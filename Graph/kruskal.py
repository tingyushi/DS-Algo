import disjoint_set
import min_heap

class WeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if not self.are_connected(node1, node2):
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
        self.weights[(node1, node2)] = weight
        self.weights[(node2, node1)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)


def kruskal(G):
    MST = WeightedGraph()
    nodes = list(G.adj.keys())
    Q = min_heap.MinHeap([])
    ds = disjoint_set.DisjointSet(nodes)

    for node in nodes:
        MST.add_node(node)
    for node in nodes:
        for neighbour in G.adj[node]:
            Q.insert(min_heap.Element((node, neighbour), G.w(node, neighbour)))

    while not Q.is_empty():
        current_edge = Q.extract_min().value
        if ds.find(current_edge[0]) != ds.find(current_edge[1]): #Nodes are not connected
            MST.add_edge(current_edge[0], current_edge[1], G.w(current_edge[0], current_edge[1]))
            ds.union(current_edge[0], current_edge[1])

    return MST