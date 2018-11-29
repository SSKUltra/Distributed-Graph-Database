from xmlrpc.server import SimpleXMLRPCServer
import uuid
import random

# function for adding edge to graph 
v_ids = {}
l_ids = {}
#e_ids = {}
graph = {}
def add_incoming_edge(u,l,v):
    if u in graph :
        graph[u].append(v)
    else :
        #adds the vertex to the graph
        graph[u] = [v]
    return graph
    
def add_outgoing_edge(u,label,v):
    return str(v_ids[u]) + str(l_ids[label]) + str(v_ids[v])

def checkVertex(u):
    if u in graph:
        return True, v_ids[u]
    else:
        graph[u] = []
        v_ids[u] = random.randint(1,1001)
        return False, v_ids[u]

def checkLabel(l):
    if l in l_ids:
        return True, l_ids[l]
    else:
        l_ids[l] = random.randint(1,1001)
        return False, l_ids[l]

def display():
    print(graph)
        
# definition of function 
def generate_edges(graph): 
    edges = [] 
  
    # for each node in graph 
    for node in graph: 
          
        # for each neighbour node of a single node 
        for neighbour in graph[node]: 
              
            # if edge exists then append 
            edges.append((node, neighbour)) 
    return edges 

server = SimpleXMLRPCServer(("192.168.1.103", 8000))
print("Listening on port 8000...")
server.register_function(add_outgoing_edge, "add_outgoing_edge")
server.register_function(add_incoming_edge, "add_incoming_edge")
server.register_function(checkVertex, "checkVertex")
server.register_function(checkLabel, "checkLabel")
server.register_function(display, "display")

server.serve_forever()