import re
"""
QUESTION 1:
Topological order requires that for every directed edge u -> v, node u
appears before node v in the output list.  DFS naturally produces this
ordering through the concept of "finish times":

  • When DFS finishes exploring all descendants of a node (i.e. it is
    about to backtrack), that node is placed at the FRONT of the result
    list (or equivalently, pushed onto a stack that is reversed at the
    end).
  • Because a node is only marked 'finished' after all nodes reachable
    from it have been visited, its finish time is always LATER than the
    finish time of any node it points to.
  • Reversing finish times therefore gives a valid topological order.

DFS also serves double duty: during the same traversal we can detect
back-edges (edges that point to an ancestor still on the current call
stack).  The presence of any back-edge proves the graph contains a cycle,
making it NOT a DAG.  If no back-edge is found, the graph is a DAG.

Time complexity: O(V + E) same as ordinary DFS.

Alternative: Kahn's algorithm (BFS-based) also works and has the same
time complexity, but DFS is slightly more elegant for simultaneous cycle
detection.
"""

class GraphNode:
    def __init__(self, data: str):
        self.data = data

    def __repr__(self):
        return f"GraphNode({self.data!r})"

class Graph:
    def __init__(self):
        self._nodes: list[GraphNode] = []
        self._adj:   dict[GraphNode, dict[GraphNode, float]] = {}

    def addNode(self, data: str) -> GraphNode:
        node = GraphNode(data)
        self._nodes.append(node)
        self._adj[node] = {}
        return node

    def removeNode(self, node: GraphNode):
        if node not in self._adj:
            return
        for neighbour in list(self._adj[node]):
            self._adj[neighbour].pop(node, None)
        del self._adj[node]
        self._nodes.remove(node)

    def addEdge(self, n1: GraphNode, n2: GraphNode,
                weight: float = 1, undirected: bool = False):
        self._adj[n1][n2] = weight
        if undirected:
            self._adj[n2][n1] = weight

    def removeEdge(self, n1: GraphNode, n2: GraphNode):
        self._adj[n1].pop(n2, None)
        self._adj[n2].pop(n1, None)

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
        self._adj.clear()
        name_to_node: dict[str, GraphNode] = {}

        def get_or_create(name: str) -> GraphNode:
            if name not in name_to_node:
                n = self.addNode(name)
                name_to_node[name] = n
            return name_to_node[name]

        edge_re = re.compile(r"(\w+)\s*--\s*(\w+)(?:\s*\[([^\]]*)\])?\s*;?")

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
            self.addEdge(n1, n2, weight, undirected=True)

        return self

    def _dfs_visit(self, node: GraphNode,
                   visited: set, on_stack: set,
                   finish_order: list) -> bool:
        visited.add(node)
        on_stack.add(node)

        for neighbour in self._adj[node]:
            if neighbour not in visited:
                if self._dfs_visit(neighbour, visited, on_stack, finish_order):
                    return True        
            elif neighbour in on_stack:
                return True           

        on_stack.discard(node)
        finish_order.append(node)      
        return False

    def isdag(self) -> bool:
        visited:  set = set()
        on_stack: set = set()

        for node in self._nodes:
            if node not in visited:
                if self._dfs_visit(node, visited, on_stack, []):
                    return False        
        return True

    def toposort(self) -> list[GraphNode] | None:
        visited:      set = set()
        on_stack:     set = set()
        finish_order: list = []
        for node in self._nodes:
            if node not in visited:
                has_cycle = self._dfs_visit(
                    node, visited, on_stack, finish_order
                )
                if has_cycle:
                    return None       
        finish_order.reverse()          
        return finish_order

    def __repr__(self):
        return (f"Graph(nodes={len(self._nodes)}, "
                f"edges={sum(len(v) for v in self._adj.values())})")

if __name__ == "__main__":

    print("=" * 60)
    print("  Exercise 5 – Topological Sort Demo")
    print("=" * 60)

    # Test 1
    print("\n[Test 1] Valid DAG")
    g = Graph()
    a = g.addNode("A")
    b = g.addNode("B")
    c = g.addNode("C")
    d = g.addNode("D")
    e = g.addNode("E")
    g.addEdge(a, b)
    g.addEdge(b, c)
    g.addEdge(b, d)
    g.addEdge(c, e)
    g.addEdge(d, e)
    print(f"  isdag()    : {g.isdag()}")       
    order = g.toposort()
    print(f"  toposort() : {[n.data for n in order]}")
    pos = {n: i for i, n in enumerate(order)}
    valid = all(pos[u] < pos[v]
                for u in g._nodes for v in g._adj[u])
    print(f"  Order valid: {valid}")    

    # Test 2
    print("\n[Test 2] Graph containing a cycle (A→B→C→A)")
    g2 = Graph()
    x = g2.addNode("X")
    y = g2.addNode("Y")
    z = g2.addNode("Z")
    g2.addEdge(x, y)
    g2.addEdge(y, z)
    g2.addEdge(z, x)   
    print(f"  isdag()    : {g2.isdag()}")      
    print(f"  toposort() : {g2.toposort()}")    

    # Test 3
    print("\n[Test 3] Disconnected DAG (two separate chains)")
    g3 = Graph()
    p = g3.addNode("P")
    q = g3.addNode("Q")
    r = g3.addNode("R")
    s = g3.addNode("S")
    g3.addEdge(p, q)    
    g3.addEdge(r, s)   
    print(f"  isdag()    : {g3.isdag()}")     
    order3 = g3.toposort()
    print(f"  toposort() : {[n.data for n in order3]}")
    pos3 = {n: i for i, n in enumerate(order3)}
    valid3 = all(pos3[u] < pos3[v]
                 for u in g3._nodes for v in g3._adj[u])
    print(f"  Order valid: {valid3}")       

    # Test 4
    print("\n[Test 4] Single-node graph")
    g4 = Graph()
    only = g4.addNode("ONLY")
    print(f"  isdag()    : {g4.isdag()}")    
    print(f"  toposort() : {[n.data for n in g4.toposort()]}")
    print("\nAll tests complete.")