import random
import time

def KruskalMST(G, W):
    n = len(G)
    T = []
    edges = []
    #read the edges from weight matrix 
    for i in range(n):
        for j in range(i+1, n):
            if(W[i][j]!=0):
                edges.append((W[i][j], i, j))
    #sort the edges by weight
    edges.sort()
    j = 0
    num_edges = 0
    # for each vertex to create individual sets, one for each vertex.
    for vertex in G:
        make_set(vertex)
    while num_edges < n-1:
        w, u, v = edges[j]
        j += 1
        if find(u) != find(v):
            T.append((u,v))
            num_edges += 1
            union(u,v)
    return T
  
# Disjoint set functions  
parent = {}
rank = {}

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(node):
    # Recursively navigate to the leader (root) node of the set
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])  # Path compression
    return parent[node]

# Define union function
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    
    # If the roots are the same, no need to merge as they are already in the same set.
    if root1 != root2:
        #add node to the smaller rank root
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            # If ranks are equal, choose one root arbitrarily and increment its rank.
            parent[root2] = root1
            rank[root1] += 1



# function to randomly Generate connected graph for test
def generate_random_connected_graph(num_vertices, num_edges, max_weight):
    # Create a list of vertices [0, 1, 2, ..., num_vertices-1]
    
    G = list(range(num_vertices))
    
    # Create an empty weight matrix
    W = [[0] * num_vertices for _ in range(num_vertices)]
    
    # Initialize the graph with a spanning tree (connected)
    for i in range(1, num_vertices):
        j = random.randint(0, i - 1)
        weight = random.randint(1, max_weight)  # Random weight between 1 and max_weight
        W[i][j] = W[j][i] = weight  # Assign random weights
    
    # Keep track of the number of added edges
    num_added_edges = num_vertices - 1
    
    # Add the remaining edges to reach the desired number of edges
    while num_added_edges < num_edges:
        i, j = random.sample(G, 2)  # Randomly select two different vertices
        if W[i][j] == 0:  # Ensure we don't overwrite existing edges
            weight = random.randint(1, max_weight)  # Random weight between 1 and max_weight
            W[i][j] = W[j][i] = weight
            num_added_edges += 1
    
    return G, W


num_vertices = 3000

num_edges = 10000
max_weight = 10
G, W = generate_random_connected_graph(num_vertices, num_edges, max_weight)
#start time
st = time.time_ns()
KruskalMST(G, W)
#end time
et = time.time_ns()
print(et-st)
        





