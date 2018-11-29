from xmlrpc.server import SimpleXMLRPCServer
import uuid
import random

v_ids = {}
l_ids = {}
graph = {}

def add_edge_src(u,v,label,v_id):
    v_ids[v] = v_id
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
        v_ids[u] = random.randint(1,1001)
        l_ids[label] = random.randint(1,1001)
    return v_ids[u], l_ids[label], graph


server = SimpleXMLRPCServer(("192.168.1.105", 8000))
print("Listening on port 8000...")
server.register_function(add_edge_src,"add_edge_src")

server.serve_forever()