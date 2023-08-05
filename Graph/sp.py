import min_heap

def dijkstra(G, source):
    pred = {} #Predecessor dictionary. 
    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, 99999))
        dist[node] = 99999
    Q.decrease_key(source, 0)

    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


def bellman_ford(G, source):
    pred = {} #Predecessor dictionary. 
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = 99999
    dist[source] = 0

    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist


'''
Bellman-Ford will iterate through all the edges of the graph V-1 times, 
potentially updating the currently known shortest distant to each node.

For the following algorithm, each node's currently known shortest distance will be updated at most k times.
dist[neighbour] = dist[node] + G.w(node, neighbour)
'''
def bellman_ford_approx(G, source, k):
    pred = {}
    dist = {} 
    updates = {}
    nodes = list(G.adj.keys())
    for node in nodes:
        dist[node] = 99999
        updates[node] = k
    dist[source] = 0
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if updates[neighbour] > 0:
                    if dist[neighbour] > dist[node] + G.w(node, neighbour):
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        updates[neighbour] = updates[neighbour] - 1
                        pred[neighbour] = node
    return dist