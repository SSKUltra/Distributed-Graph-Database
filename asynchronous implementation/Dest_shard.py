from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import uuid
import random

with xmlrpc.client.ServerProxy("http://192.168.1.105:8000/") as proxy:
    v_ids = {}
    l_ids = {}
    graph = {}
    
    def add_edge_dst(u,v,label):
        count = 1
        if v in graph:
            pass
        else:
            graph[v] = []
            v_ids[v] = random.randint(1,1001)
        
        v_ids[u],l_ids[label], graph_source = proxy.add_edge_src(u,v,label,v_ids[v])
        count += 2
        return graph_source, count

    # graph1 = add_edge_dst('u','v','connects')
    # print(graph1)
    server = SimpleXMLRPCServer(("192.168.1.103", 8000))
    print("Listening on port 8000...")
    server.register_function(add_edge_dst,"add_edge_dst")

    server.serve_forever()