class Node:
    def __init__(self, data):
        self.data = data    # node identifier

class Graph:
    def __init__(self):
        self.vertices =  {}       # dict of vertices, {Node("A"): self.edges[0], Node("B"): self.edges[1]}  node keys for pointers to respective adjacency list in self.edges
        self.edges = [ [] for i in range(len(self.vertices)) ]      # format: [ [(n2, weight), (n3, weight)] , [(n4, weight), (n5, weight)]] 
                                                                    # each tuple stores neighbor and weight, tuples are stored in sublist per node

    def addNode(self, data): 
        '''
        creates a new graph node internally storing the string
passed as parameter. Returns a GraphNode object
        '''
        for node in self.vertices:
            if node.data == data:
                return False
            
        new_node = Node(data)
        self.edges.append([])       # creates new adjacency list for new node
        self.vertices[new_node] = self.edges[-1]        # places new node in dict, value is pointer to respective adjacency list in self.edges
        return new_node    # returns new node made


    def removeNode(self, node):
        '''
        removes nodes
        '''
        if node not in self.vertices:
            return False

        adj_list = self.vertices[node]      # get node-to-be-removed's adjacency list
        del self.vertices[node]             # remove node from self.vertices then remove its adjacency list
        self.edges.remove(adj_list)

        for list in self.edges:     # remove every tuple (edge connection) with reference to deleted node in all adjacency lists
            to_remove = []
            for edge in list:
                if node in edge:
                    to_remove.append(edge)
            for edge in to_remove:
                list.remove(edge)


    def addEdge(self, n1, n2, weight):
        '''
        creates an edge between nodes n1 and n2
        ''' # possibly check for node existence before creating edge
        if n1 not in self.vertices or n2 not in self.vertices:
            return -1       # fail
        
        self.vertices[n1].append((n2, weight))   # append to each involved nodes adjacency list
        self.vertices[n2].append((n1, weight))   # self.vertices is dict, so use nodes as keys, append to adjacency lists

    def removeEdge(self, n1, n2):
        '''
        removes the edge between nodes n1 and n2
        '''
        if n1 not in self.vertices or n2 not in self.vertices:
            return False

        n1_list = self.vertices[n1]         # take adjacency lists of involved nodes
        n2_list = self.vertices[n2]

        for edge in n1_list:               # for each edge in involved nodes lists, remove edge with other node
            if n2 in edge:
                n1_list.remove(edge)
                break

        for edge in n2_list:
            if n1 in edge:
                n2_list.remove(edge)
                break



    def importFromFile(self, file):
        '''
        imports a graph description from a GraphViz
file. GraphViz files define a simple format for graph description. You will not
need to implement all the features of GraphViz, only basic ones described
below. The method clears all existing nodes and edges, and replaces them
with those listed in the file.

        '''
        self.vertices = {}
        self.edges = []
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                
                if not lines[0].strip() == 'strict graph G {':
                    return None
                
                for line in lines[1:]:
                    line = line.strip()

                    if line == '}':
                        break

                    if '--' not in line:
                        return None

                    parts = line.split('--')        # split line at '--'
                    n1 = parts[0].strip()           # strips whitespace from first half of line, stores first node
                    n2 = parts[1].split('[')[0].strip()         # splits second half of line at '[', strips whitespace from left of '[', stores as second node

                    if 'weight=' in line:
                        weight = int(line.split('weight=')[1].split(']')[0])        # stores weight found between 'weight=' and ']' in line
                    else:
                        weight = 1      # otherwise if no weight in edge, assume weight = 1

                    node1 = None
                    node2 = None

                    for node in self.vertices:
                        if node.data == n1:
                            node1 = node
                        if node.data == n2:
                            node2 = node
                        if node1 and node2:
                            break
                    
                    if node1 is None:
                        node1 = self.addNode(n1)
                    
                    if node2 is None:
                        node2 = self.addNode(n2)

                    self.addEdge(node1, node2, weight)
        
        except:
            return None
