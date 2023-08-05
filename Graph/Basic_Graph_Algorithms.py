from collections import deque

'''
BFS and DFS: just return true or false
BFS2 and DFS2: return list indicating path
BFS3 and DFS3: return a dictionary as predecessor map
'''

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


# undirected weighted graph
class WeightedGraph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        for edge in self.adj[node1]:
            if edge[0] == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2, weight):
        if node1 not in self.adj[node2]:
            self.adj[node1].append((node2, weight))
            self.adj[node2].append((node1, weight))

    def w(self, node1, node2):
        for edge_info in self.adj[node1]:
            if node2 == edge_info[0]:
                return edge_info[1]

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


def BFS2(G, node1, node2):
    #exception handling
    if G.number_of_nodes() == 0:
        return []
    if not BFS(G, node1, node2):
        return []
    if (node1 == node2):
        return [node1]

    #mark nodes
    pred = {}
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    
    flag = True

    #create predcessor dictionary
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2 and flag:#once node2 is found for the first time, predecessor table is finished
                flag = False
                pred[node] = current_node
                final_pred = pred.copy()
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                pred[node] = current_node

    #search in predcessor dictionay 
    path = [node2]
    parent = final_pred[node2]
    while parent != node1:
        path.insert(0, parent)
        parent = final_pred[parent]
    path.insert(0, node1)
    
    return path



def DFS2(G, node1, node2):
    if G.number_of_nodes() == 0:
        return []
    if not DFS(G, node1, node2):
        return []
    if (node1 == node2):
        return [node1]

    pred = {}
    S = [node1]
    marked = {}
    for n in G.adj:
        marked[n] = False
    
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for n in G.adj[current_node]:
                S.append(n)
                if not marked[n]:
                    if n not in pred: #if predcessor exists, nothing happens
                        pred[n] = current_node            
    
    path = []
    temp = node2
    while temp != node1:
        path.insert(0, temp)
        temp = pred[temp]
    path.insert(0, node1)
    return path



def BFS3(G, node):
    if G.number_of_nodes() == 0:
        return
    
    pred = {}
    Q = deque([node])
    marked = {}

    for n in G.adj:
        marked[n] = False

    while len(Q) != 0:
        current_node = Q.popleft()
        marked[current_node] = True #mark visited
        for n in G.adj[current_node]:
            if not marked[n]: #the nodes that are not visted
                Q.append(n)
                if n not in pred:
                    pred[n] = current_node
    return pred



def DFS3(G, node):
    pred = {}
    S = [node]
    marked = {}
    for n in G.adj:
        marked[n] = False
    
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for n in G.adj[current_node]:
                S.append(n)
                if not marked[n]:
                    if n not in pred: #if predcessor exists, nothing happens
                        pred[n] = current_node            
    return pred


def is_connected(G):
    for i in G.adj:
        for j in G.adj:
            if (i != j):
                if not BFS(G, i, j):
                    return False
    return True


def has_cycle_helper(G, node1):
    S = [node1]
    marked = {}
    pred = {}

    for node in G.adj:
        marked[node] = False
    
    while len(S) != 0:
        current_node = S.pop()
        #print(current_node)
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if not marked[node]:
                    pred[node] = current_node
                S.append(node)
                if marked[node] and node != pred[current_node]:
                    return True
    return False


def has_cycle(G):

    if G.number_of_nodes() == 0:
        return False

    for i in G.adj:
        if has_cycle_helper(G, i):
            return True
    return False