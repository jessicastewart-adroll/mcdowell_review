### correctly handle starting node
'''
undirected graph 
distance between nodes is always 6
s - starting node
queries - graph, starting node
get shortest distance from starting node to all the other nodes in the graph. Then print a single line of  space-separated integers listing node 's shortest distance to each of the  other nodes (
ordered sequentially by node number
if disconnected, print -1

first line - number of queries
second line - number of nodes and number of edges in the graph
subsequent lines - edge connecting nodes 
last line - index of starting node

for each query - print space-separated integers denoting the shortest distances to each node from starting position
listed sequentially by node number but not include node

Sample Input
2
4 2
1 2
1 3
1
3 1
2 3
2
Sample Output
6 6 -1
-1 6

DISTANCE = 6
UNREACHABLE = -1
'''
from collections import defaultdict

class Graph(object):
	def __init__(self, node_count):
		self.node_count = node_count
		self.adjacency_matrix = defaultdict(self.create_list)
		for node in range(1, self.node_count+1):
			self.adjacency_matrix[node]

	@staticmethod		
	def create_list():
		return []		

	def connect(self, x, y):
		self.adjacency_matrix[x].append(y)
		self.adjacency_matrix[y].append(x)

	def	find_all_distances(self, start_node):
		def bfs(start_node, end_node, distance):
			if start_node in self.adjacency_matrix[end_node]:
				return distance	
			for node in self.adjacency_matrix[end_node]:
				return bfs(start_node, node, distance+6)	
	

		result = []
		for end_node in range(1, self.node_count+1):
			distance = 6
			if not self.adjacency_matrix[end_node]:
				result.append('-1')
			elif start_node in self.adjacency_matrix[end_node]:
				result.append(str(distance))
			elif start_node == end_node:
				continue
			else:	
				distance = bfs(start_node, end_node, distance)
				result.append(str(distance))
		print(' '.join(result))			


# t = int(input())
# for i in range(t):
#     node_count, edge_count = [int(value) for value in input().split()]
#     graph = Graph(node_count)
#     for i in range(edge_count):
#         edge_x,edge_y = [int(edge_x) for edge_x in input().split()]
#         graph.connect(edge_x,edge_y) 
#     starting_node = int(input())
#     graph.find_all_distances(starting_node)

# g1 = Graph(4)
# e1 = [(1, 2), (1, 3)]
# for x, y in e1:
# 	g1.connect(x, y)
# g1.find_all_distances(1)	

# g2 = Graph(3)
# e2 = [(2, 3)]
# for x, y in e2:
# 	g2.connect(x, y)
# g2.find_all_distances(2)

g2 = Graph(4)
e2 = [(2, 3), (2, 4)]
for x, y in e2:
	g2.connect(x, y)
g2.find_all_distances(4)
# -1 6 12	
    

'''
undirected graph 
distance between nodes is always 6
s - starting node
queries - graph, starting node
get shortest distance from starting node to all the other nodes in the graph. Then print a single line of  space-separated integers listing node 's shortest distance to each of the  other nodes (
ordered sequentially by node number
if disconnected, print -1

first line - number of queries
second line - number of nodes and number of edges in the graph
subsequent lines - edge connecting nodes 
last line - index of starting node

for each query - print space-separated integers denoting the shortest distances to each node from starting position
listed sequentially by node number but not include node

Sample Input
2
4 2
1 2
1 3
1
3 1
2 3
2
Sample Output
6 6 -1
-1 6

DISTANCE = 6
UNREACHABLE = -1
'''
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
