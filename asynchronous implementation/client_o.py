#source shard
import xmlrpc.client
import networkx as nx
import matplotlib.pyplot as plt

with xmlrpc.client.ServerProxy("http://192.168.1.103:8000/") as proxy:
	# function for adding edge to graph 

	graph = {}

	def generate_edges(graph):
		edges = []

		for node in graph:

			for neighbour in graph[node]:

				edges.append((node, neighbour))

		return edges
	  
	# definition of function 
	n = int(input("Enter number of edges to be added:"))
	i = 0

	while(i<n):

		u = input("Enter source vertex: ")

		v = input("Enter target vertex: ")
		
		l = input("Enter label name: ")

		graph = proxy.add_edge_dst(u,l,v)

		# print(generate_edges(graph)) 
		i = i + 1

	print(graph)
	edge_representation = generate_edges(graph)
	print(edge_representation)


	

	G = nx.DiGraph()

	# G.add_edges_from([('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])


	G.add_edges_from(edge_representation)
	val_map = {'A': 1.0,
	           'D': 0.5714285714285714,
	           'H': 0.0}

	values = [val_map.get(node, 0.25) for node in G.nodes()]

	# Specify the edges you want here
	red_edges = []
	edge_colours = ['black' if not edge in red_edges else 'red'
	                for edge in G.edges()]
	black_edges = [edge for edge in G.edges() if edge not in red_edges]

	# Need to create a layout when doing
	# separate calls to draw nodes and edges
	pos = nx.spring_layout(G)
	nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = values, node_size = 500)
	nx.draw_networkx_labels(G, pos)
	nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
	nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
	plt.show()