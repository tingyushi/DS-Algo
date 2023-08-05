from Basic_Graph_Algorithms import WeightedGraph
from min_heap import *

# does not use min heap
def prim1(G):
    if (G.number_of_nodes() <= 2):
        return G
    edges = prim1_helper(G, 0)

    ansG = WeightedGraph(G.number_of_nodes())
    for ele in edges:
        ansG.add_edge(ele[0], ele[1], ele[2])
    return ansG


def prim1_helper(G, root):
    number_of_nodes = len(G.adj)
    visted = set()
    selected_edges = [] #Theses are edges for the new graph -> (node1, node2, weight)
    current_node = root
    while True:
        visted.add(current_node)
        min_edge = get_min_edge(G, visted)
        current_node = min_edge[1]
        selected_edges.append(min_edge)
        if len(selected_edges) == number_of_nodes - 1:
            return selected_edges


def get_min_edge(G, s):
    all_neighbour = [] #(parent, neighbour, weight)
    for visted_node in s:
        temp = G.adj[visted_node]
        for n in temp:
            if n[0] not in s:
                all_neighbour.append((visted_node, n[0], n[1]))
    min_edge = all_neighbour[0]
    min_weight = all_neighbour[0][2]
    for i in all_neighbour:
        if (i[2] < min_weight):
            min_weight = i[2]
            min_edge = i
    return min_edge #(parent, neighbor, weight)
    

# use min heap
def prim2(G):
    if (G.number_of_nodes() <= 2):
        return G
    edges = prim2_helper(G, 0)
    ansG = WeightedGraph(G.number_of_nodes())
    for ele in edges:
        ansG.add_edge(ele[0], ele[1], ele[2])
    return ansG


def prim2_helper(G, root):
    heap = MinHeap([])
    #build heap
    for n in G.adj:
        if not (n == root):
            heap.insert(Element(n, 1500))

    selected_edges = []
    current_node = root
    visited = set()

    while True:
        visited.add(current_node)
        for n in G.adj[current_node]:
            if n[0] not in visited:
                heap.decrease_key(n[0], n[1])
        temp = heap.extract_min() #Element object

        #find parent
        for n in G.adj[temp.value]:
            if n[1] == temp.key:
                parent = n[0]
        selected_edges.append((parent, temp.value, temp.key))
        current_node = temp.value
        if (len(selected_edges) == G.number_of_nodes() - 1):
            return selected_edges