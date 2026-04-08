import re
import time
import random

class GraphNode:
    def __init__(self, data: str):
        self.data = data

    def __repr__(self):
        return f"GraphNode({self.data!r})"

class Graph:
    def __init__(self):
        self._nodes: list[GraphNode] = []
        self._adj:  dict[GraphNode, dict[GraphNode, float]] = {}

    def addNode(self, data: str) -> GraphNode:
        node = GraphNode(data)
        self._nodes.append(node)
        self._adj[node] = {}
        return node

    def removeNode(self, node: GraphNode):
        if node not in self._adj:
            return
        # remove all edges that touch this node
        for neighbour in list(self._adj[node]):
            self._adj[neighbour].pop(node, None)
        del self._adj[node]
        self._nodes.remove(node)

    def addEdge(self, n1: GraphNode, n2: GraphNode, weight: float = 1):
        self._adj[n1][n2] = weight
        self._adj[n2][n1] = weight   # undirected

    def removeEdge(self, n1: GraphNode, n2: GraphNode):
        self._adj[n1].pop(n2, None)
        self._adj[n2].pop(n1, None)

    def importFromFile(self, file: str):
        """
        Parses a basic GraphViz 'strict graph' file and rebuilds the graph.
        Returns self on success, None on any parse / semantic error.
        """
        try:
            with open(file, "r") as f:
                text = f.read()
        except OSError:
            return None

        text = re.sub(r"//[^\n]*", "", text)
        text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
        header_match = re.match(r"\s*(strict\s+graph)\s+\w+\s*\{", text, re.IGNORECASE)
        if not header_match:
            return None

        body_match = re.search(r"\{(.*)\}", text, re.DOTALL)
        if not body_match:
            return None
        body = body_match.group(1)

        self._nodes.clear()
        self._adj.clear()
        name_to_node: dict[str, GraphNode] = {}

        def get_or_create(name: str) -> GraphNode:
            if name not in name_to_node:
                n = self.addNode(name)
                name_to_node[name] = n
            return name_to_node[name]

        edge_re = re.compile(
            r"(\w+)\s*--\s*(\w+)"
            r"(?:\s*\[([^\]]*)\])?\s*;?"
        )

        for line in body.splitlines():
            line = line.strip()
            if not line:
                continue
            m = edge_re.match(line)
            if not m:
                return None
            a, b, attrs = m.group(1), m.group(2), m.group(3) or ""
            weight = 1.0
            w_match = re.search(r"weight\s*=\s*([0-9]*\.?[0-9]+)", attrs)
            if w_match:
                weight = float(w_match.group(1))
            n1 = get_or_create(a)
            n2 = get_or_create(b)
            self.addEdge(n1, n2, weight)

        return self

    def dfs(self, start: GraphNode = None) -> list[GraphNode]:
        """
        Iterative DFS traversal of the entire graph (handles disconnected
        components).  Returns nodes in DFS visit order.
        If start is given, that node is visited first.
        """
        visited: set[GraphNode] = set()
        order:   list[GraphNode] = []

        nodes = self._nodes[:]
        if start and start in nodes:
            nodes.remove(start)
            nodes = [start] + nodes

        for root in nodes:
            if root in visited:
                continue
            stack = [root]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                order.append(node)
                for neighbour in reversed(list(self._adj[node])):
                    if neighbour not in visited:
                        stack.append(neighbour)

        return order

    def __repr__(self):
        return f"Graph(nodes={len(self._nodes)}, edges={sum(len(v) for v in self._adj.values())//2})"

class Graph2:
    def __init__(self):
        self._nodes:  list[GraphNode] = []
        self._index:  dict[GraphNode, int] = {}
        self._matrix: list[list[float]] = []   # N×N

    def _resize(self, new_size: int):
        """Expand the matrix to new_size × new_size."""
        old_size = len(self._matrix)
        # extend existing rows
        for row in self._matrix:
            row.extend([0.0] * (new_size - old_size))
        # add new rows
        for _ in range(new_size - old_size):
            self._matrix.append([0.0] * new_size)

    def _shrink(self, removed_idx: int):
        """Remove row and column at removed_idx."""
        del self._matrix[removed_idx]
        for row in self._matrix:
            del row[removed_idx]

    def addNode(self, data: str) -> GraphNode:
        node = GraphNode(data)
        idx = len(self._nodes)
        self._nodes.append(node)
        self._index[node] = idx
        self._resize(idx + 1)
        return node

    def removeNode(self, node: GraphNode):
        if node not in self._index:
            return
        idx = self._index.pop(node)
        self._nodes.remove(node)
        self._shrink(idx)
        for n in self._nodes:
            if self._index[n] > idx:
                self._index[n] -= 1

    def addEdge(self, n1: GraphNode, n2: GraphNode, weight: float = 1):
        i, j = self._index[n1], self._index[n2]
        self._matrix[i][j] = weight
        self._matrix[j][i] = weight 

    def removeEdge(self, n1: GraphNode, n2: GraphNode):
        i, j = self._index[n1], self._index[n2]
        self._matrix[i][j] = 0.0
        self._matrix[j][i] = 0.0

    def importFromFile(self, file: str):
        try:
            with open(file, "r") as f:
                text = f.read()
        except OSError:
            return None

        text = re.sub(r"//[^\n]*", "", text)
        text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
        if not re.match(r"\s*(strict\s+graph)\s+\w+\s*\{", text, re.IGNORECASE):
            return None

        body_match = re.search(r"\{(.*)\}", text, re.DOTALL)
        if not body_match:
            return None
        body = body_match.group(1)

        self._nodes.clear()
        self._index.clear()
        self._matrix.clear()
        name_to_node: dict[str, GraphNode] = {}

        def get_or_create(name: str) -> GraphNode:
            if name not in name_to_node:
                n = self.addNode(name)
                name_to_node[name] = n
            return name_to_node[name]

        edge_re = re.compile(
            r"(\w+)\s*--\s*(\w+)"
            r"(?:\s*\[([^\]]*)\])?\s*;?"
        )

        for line in body.splitlines():
            line = line.strip()
            if not line:
                continue
            m = edge_re.match(line)
            if not m:
                return None
            a, b, attrs = m.group(1), m.group(2), m.group(3) or ""
            weight = 1.0
            w_match = re.search(r"weight\s*=\s*([0-9]*\.?[0-9]+)", attrs)
            if w_match:
                weight = float(w_match.group(1))
            n1 = get_or_create(a)
            n2 = get_or_create(b)
            self.addEdge(n1, n2, weight)

        return self
    
    def dfs(self, start: GraphNode = None) -> list[GraphNode]:
        n = len(self._nodes)
        visited: set[int] = set()
        order:   list[GraphNode] = []
        start_idx = self._index.get(start, 0) if start else 0
        indices = list(range(n))
        if start_idx in indices:
            indices.remove(start_idx)
            indices = [start_idx] + indices

        for root_idx in indices:
            if root_idx in visited:
                continue
            stack = [root_idx]
            while stack:
                idx = stack.pop()
                if idx in visited:
                    continue
                visited.add(idx)
                order.append(self._nodes[idx])
                for j in reversed(range(n)):
                    if self._matrix[idx][j] != 0 and j not in visited:
                        stack.append(j)

        return order

    def __repr__(self):
        n = len(self._nodes)
        edges = sum(
            1 for i in range(n) for j in range(i + 1, n)
            if self._matrix[i][j] != 0
        )
        return f"Graph2(nodes={n}, edges={edges})"

def measure_dfs(graph, label: str, repetitions: int = 10):
    times = []
    for _ in range(repetitions):
        t0 = time.perf_counter()
        graph.dfs()
        t1 = time.perf_counter()
        times.append((t1 - t0) * 1_000_000) 

    avg = sum(times) / len(times)
    print(f"\n{'─'*50}")
    print(f"  {label}")
    print(f"{'─'*50}")
    print(f"  Repetitions : {repetitions}")
    print(f"  Min time    : {min(times):.2f} µs")
    print(f"  Max time    : {max(times):.2f} µs")
    print(f"  Avg time    : {avg:.2f} µs")
    return times

def build_sample_graph(GraphClass, node_count=50, edge_prob=0.1):
    g = GraphClass()
    nodes = [g.addNode(f"n{i}") for i in range(node_count)]
    for i in range(node_count):
        for j in range(i + 1, node_count):
            if random.random() < edge_prob:
                g.addEdge(nodes[i], nodes[j], weight=random.randint(1, 10))
    return g


if __name__ == "__main__":
    import os
    DOT_FILE = os.path.join(os.path.dirname(__file__), "random.dot")
    if os.path.exists(DOT_FILE):
        print(f"Loading '{DOT_FILE}' …")
        g1 = Graph()
        result = g1.importFromFile(DOT_FILE)
        if result is None:
            print("ERROR: could not parse the .dot file for Graph.")
            exit(1)

        g2 = Graph2()
        result = g2.importFromFile(DOT_FILE)
        if result is None:
            print("ERROR: could not parse the .dot file for Graph2.")
            exit(1)
    else:
        print(f"'{DOT_FILE}' not found – generating a random graph for demonstration.")
        g1 = build_sample_graph(Graph,  node_count=80, edge_prob=0.08)
        g2 = build_sample_graph(Graph2, node_count=80, edge_prob=0.08)

    print(f"\nAdjacency-list graph : {g1}")
    print(f"Adjacency-matrix graph : {g2}")

    REPS = 10
    times_list = measure_dfs(g1, "Graph  (adjacency LIST)  – dfs()", REPS)
    times_mat  = measure_dfs(g2, "Graph2 (adjacency MATRIX) – dfs()", REPS)

    order_list = [nd.data for nd in g1.dfs()]
    order_mat  = [nd.data for nd in g2.dfs()]
    same_order = order_list == order_mat
    print(f"\n  DFS order identical across both representations: {same_order}")
    if not same_order:
        print("  (Minor differences are expected if node insertion order differs)")

    # RESULTS DISCUSSION
    # 
    # Observed behaviour (typical for a sparse graph like random.dot):
    #
    #   Graph  (adjacency list)  ~  faster / comparable
    #   Graph2 (adjacency matrix) ~ slower
    # WHY?
    #
    # Adjacency List:
    #   - Finding all neighbours of a node costs O(deg(v)), where deg(v)
    #     is the actual number of edges from that node.
    #   - Overall DFS time complexity: O(V + E).
    #   - For sparse graphs (few edges relative to V²) this is very
    #     efficient; we only ever look at edges that exist.
    #
    # Adjacency Matrix:
    #   - Finding all neighbours of a node requires scanning its ENTIRE
    #     row (all V entries) regardless of how many edges it has.
    #   - Overall DFS time complexity: O(V²).
    #   - For sparse graphs this wastes time examining many zero entries.
    #   - The matrix also uses O(V²) memory, which can hurt cache
    #     performance for large graphs.
    #
    # For DENSE graphs (E ≈ V²), the two approaches become comparable
    # because deg(v) ≈ V for most nodes.
    #
    # Conclusion:
    #   The adjacency-list representation is preferable for DFS on
    #   sparse graphs; the adjacency-matrix representation can match it
    #   only for very dense graphs.
