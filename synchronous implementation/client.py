import xmlrpc.client

with xmlrpc.client.ServerProxy("http://192.168.1.103:8000/") as proxy:
	# function for adding edge to graph 

	graph = {}
	  
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
	  
	def v_exists(vertex_status,v,name):
		if vertex_status == True:
			print('Vertex ' + name + ' with id ' + str(v) + ' already exists')
		else:
			print('New vertex ' + name + ' with id ' + str(v) + ' is created')


	def l_exists(label_status,l,name):
		if label_status == True:
			print('Label ' + name + ' with id ' + str(l) + ' already exists')
		else:
			print('New Label ' + name + ' with id ' + str(l) + ' is created')
	
	n = int(input("Enter number of edges to be added:"))
	i = 0

	while(i<n):

		u = input("Enter source vertex: ")

		vertex_status,vids = proxy.checkVertex(u)
		v_exists(vertex_status,vids,u)

		v = input("Enter target vertex: ")
		
		vertex_status,vidt = proxy.checkVertex(v)
		v_exists(vertex_status,vidt,v)

		l = input("Enter label name: ")

		label_status,lid = proxy.checkLabel(l)
		l_exists(label_status,lid,l)

		e_id=proxy.add_outgoing_edge(u,l,v)
		print('Edge id ' + str(e_id) + ' is created')

		graph = proxy.add_incoming_edge(u,l,v)

		# print(generate_edges(graph)) 
		i = i + 1

	print(graph)


