
class GraphNode:
    def __init__(self, name):
        self.name = str(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def makeSet(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)

        if root1 == root2:
            return False

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}  

    def addNode(self, name):
        node = GraphNode(name)
        self.nodes.append(node)
        self.edges[node] = []
        return node

    def getNode(self, name):
        for n in self.nodes:
            if n.name == str(name):
                return n
        return None

    def addEdge(self, n1, n2, w=1):
        if n1 not in self.edges or n2 not in self.edges:
            return

        for nei, _ in self.edges[n1]:
            if nei == n2:
                return

        self.edges[n1].append((n2, w))
        self.edges[n2].append((n1, w))

    def importFromFile(self, filename):
        try:
            f = open(filename, "r")
            lines = f.readlines()
            f.close()
        except:
            return None

        self.nodes = []
        self.edges = {}

        if len(lines) == 0:
            return None

        cleaned = []
        for line in lines:
            line = line.strip()
            if line != "":
                cleaned.append(line)

        if cleaned[0] != "strict graph G {":
            return None

        if cleaned[-1] != "}":
            return None

        for line in cleaned[1:-1]:
            if not line.endswith(";"):
                return None

            line = line[:-1].strip()
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

            if "--" not in edge_part:
                return None

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

    def getAllEdges(self):
        all_edges = []
        seen = set()

        for n in self.nodes:
            for nei, w in self.edges[n]:
                key = tuple(sorted([n.name, nei.name]))
                if key not in seen:
                    seen.add(key)
                    all_edges.append((n, nei, w))

        return all_edges


    def mst(self):
        tree = Graph()


        for n in self.nodes:
            tree.addNode(n.name)

        uf = UnionFind()
        for n in self.nodes:
            uf.makeSet(n)

        edges = self.getAllEdges()
        edges.sort(key=lambda x: x[2]) 

        for n1, n2, w in edges:
            if uf.union(n1, n2):
                t1 = tree.getNode(n1.name)
                t2 = tree.getNode(n2.name)
                tree.addEdge(t1, t2, w)

        return tree


    def printGraph(self, limit=100):
        printed = set()
        count = 0

        for n in self.nodes:
            for nei, w in self.edges[n]:
                key = tuple(sorted([n.name, nei.name]))
                if key not in printed:
                    printed.add(key)
                    print(n.name, "--", nei.name, "weight =", w)

                    count += 1
                    if count >= limit:
                        print("first 100")
                        return


def main():
    g = Graph()

    if g.importFromFile("random.dot") is None:
        print("load error")
        return

    print("MST edges (first 100):")
    tree = g.mst()
    tree.printGraph(100)


if __name__ == "__main__":
    main()