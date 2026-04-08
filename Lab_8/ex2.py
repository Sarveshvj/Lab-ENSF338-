# Q1:
# Two ways to do it 
# one is simple list / set and use linear search every time to find the smallest distance. and is slower because finding the minimum takes O(n).
# two is a priority queue (heap). this is faster because removing the smallest element is more efficient.
import time
import heapq
import matplotlib.pyplot as plt


class GraphNode:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, name):
        node = GraphNode(name)
        self.nodes.append(node)
        self.edges[node] = []
        return node

    def addEdge(self, n1, n2, w=1):
        if n1 not in self.edges or n2 not in self.edges:
            return


        for nei, _ in self.edges[n1]:
            if nei == n2:
                return

        self.edges[n1].append((n2, w))
        self.edges[n2].append((n1, w))

    def getNode(self, name):
        for n in self.nodes:
            if n.name == name:
                return n
        return None

    def importFromFile(self, filename):
        try:
            f = open(filename, "r")
            lines = f.readlines()
            f.close()
        except:
            return None

        self.nodes = []
        self.edges = {}

        if lines[0].strip() != "strict graph G {":
            return None

        for line in lines[1:-1]:
            line = line.strip()
            if line == "":
                continue

            if not line.endswith(";"):
                return None

            line = line[:-1]

            weight = 1

            if "[" in line:
                parts = line.split("[")
                edge_part = parts[0].strip()
                attr = parts[1].strip()

                attr = attr[:-1] 
                if attr.startswith("weight="):
                    weight = int(attr.split("=")[1])
                else:
                    return None
            else:
                edge_part = line

            a, b = edge_part.split("--")
            a = a.strip()
            b = b.strip()

            n1 = self.getNode(a)
            if n1 is None:
                n1 = self.addNode(a)

            n2 = self.getNode(b)
            if n2 is None:
                n2 = self.addNode(b)

            self.addEdge(n1, n2, weight)

        return self

    def slowSP(self, start):
        dist = {}
        visited = set()

        for n in self.nodes:
            dist[n] = float("inf")
        dist[start] = 0

        while len(visited) < len(self.nodes):
            cur = None
            best = float("inf")

            for n in self.nodes:
                if n not in visited and dist[n] < best:
                    cur = n
                    best = dist[n]

            if cur is None:
                break

            visited.add(cur)

            for nei, w in self.edges[cur]:
                if nei not in visited:
                    if dist[cur] + w < dist[nei]:
                        dist[nei] = dist[cur] + w

        return dist

    def fastSP(self, start):
        dist = {}
        visited = set()
        pq = []
        count = 0

        for n in self.nodes:
            dist[n] = float("inf")
        dist[start] = 0

        heapq.heappush(pq, (0, count, start))
        count += 1

        while pq:
            d, _, cur = heapq.heappop(pq)

            if cur in visited:
                continue

            visited.add(cur)

            for nei, w in self.edges[cur]:
                new_d = d + w
                if new_d < dist[nei]:
                    dist[nei] = new_d
                    heapq.heappush(pq, (new_d, count, nei))
                    count += 1

        return dist


def measure(graph):
    slow = []
    fast = []

    for n in graph.nodes:
        t1 = time.perf_counter()
        graph.slowSP(n)
        t2 = time.perf_counter()
        slow.append(t2 - t1)

    for n in graph.nodes:
        t1 = time.perf_counter()
        graph.fastSP(n)
        t2 = time.perf_counter()
        fast.append(t2 - t1)

    return slow, fast


def stats(name, arr):
    print(name)
    print("avg:", sum(arr) / len(arr))
    print("max:", max(arr))
    print("min:", min(arr))
    print()


def plot(slow, fast):
    plt.hist(slow)
    plt.title("slowSP")
    plt.show()

    plt.hist(fast)
    plt.title("fastSP")
    plt.show()


def main():
    g = Graph()
    if g.importFromFile("random.dot") is None:
        print("load error")
        return

    slow, fast = measure(g)

    stats("slowSP", slow)
    stats("fastSP", fast)

    plot(slow, fast)

 # Q4
# In my test, fastSP is much faster than slowSP.
# This is because slowSP uses linear search to find the next node, which takes O(n) time each iteration,
# and fastSP uses a heap priority queue, which is faster.

# From the histograms:
# - slowSP has a wider spread, meaning its performance varies more.
# - fastSP is more concentrated, meaning it is more consistent. also has much smaller execution times overall.

# from this we can see that fastSP is both faster and more stable, especially for a larger graphs.

if __name__ == "__main__":
    main()