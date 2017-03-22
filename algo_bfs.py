from collections import defaultdict

class Graph(object):
	def __init__(self, node_count):
		self.node_count = node_count
		self.adjacency_matrix = defaultdict(self.create_list)
		for node in range(1, self.node_count+1):
			self.adjacency_matrix[node_count]

	@staticmethod		
	def create_list():
		return []		

	def connect(self, x, y):
		self.adjacency_matrix[x].append(y)
		self.adjacency_matrix[y].append(x)

	def	find_all_distances(self, starting_node):
		result = []
		for edge in range(1, self.node_count+1):
			if edge == starting_node:
				for node in self.adjacency_matrix[starting_node]:
					result.append('6')
			else:
				if not self.adjacency_matrix[edge]:
					result.append('-1')	

		print(' '.join(result))	

t = int(input())
for i in range(t):
    node_count, edge_count = [int(value) for value in input().split()]
    graph = Graph(node_count)
    for i in range(edge_count):
        edge_x,edge_y = [int(edge_x) for edge_x in input().split()]
        graph.connect(edge_x,edge_y) 
    starting_node = int(input())
    graph.find_all_distances(starting_node)
