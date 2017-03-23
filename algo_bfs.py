### get each distinct path
from collections import defaultdict, deque

class Graph(object):
	def __init__(self, node_count):
		self.node_count = node_count
		self.graph = defaultdict(list)
		for node in range(1, self.node_count+1):
			self.graph[node]

	def connect(self, x, y):
		self.graph[x].append(y)
		self.graph[y].append(x)

	def	find_all_distances(self, start_node):
		print(self.graph)
		visited = [False]*(len(self.graph)+1)
		queue = deque()

		queue.append(start_node)

		while queue:
			val = queue.popleft()
			print(val)
			visited[val] = True

			for i in self.graph[val]:
				if not visited[i]:
					queue.append(i)

	def	find_path(self, start_node, end_node):
		print(self.graph)
		visited = [False]*(len(self.graph)+1)
		queue = deque()

		queue.append(start_node)

		while queue:
			val = queue.popleft()
			print(val)
			visited[val] = True
			if val == end_node:
				return

			for i in self.graph[val]:
				if not visited[i]:
					queue.append(i)

	def bfs(self, start, end):
		print('start', start, 'end', end)
		queue = deque()
		
		visited = [False]*(len(self.graph)+1)
		queue.append(start)

		while queue:
			val = queue.popleft()
			print(val)
			visited[val] = True
			if val == end:
				return

			for i in self.graph[val]:
				if not visited[i]:
					queue.append(i)		

	def	find_all_pathes(self, end):
		for n in self.graph:
			if not n==end:
				self.bfs(n, end)	

# t = int(input())
# for i in range(t):
#     node_count, edge_count = [int(value) for value in input().split()]
#     graph = Graph(node_count)
#     for i in range(edge_count):
#         edge_x,edge_y = [int(edge_x) for edge_x in input().split()]
#         graph.connect(edge_x,edge_y) 
#     starting_node = int(input())
#     graph.find_all_distances(starting_node)

g1 = Graph(4)
e1 = [(1, 2), (1, 3)]
for x, y in e1:
	g1.connect(x, y)
g1.find_all_distances(1)	

g2 = Graph(3)
e2 = [(2, 3)]
for x, y in e2:
	g2.connect(x, y)
g2.find_all_distances(2)

g3 = Graph(4)
e3 = [(2, 3), (2, 4)]
for x, y in e3:
	g3.connect(x, y)
g3.find_all_distances(4)
# -1 6 12	

g3 = Graph(4)
e3 = [(1, 2), (2, 3), (3, 4), (4, 1)]
for x, y in e3:
	g3.connect(x, y)
g3.find_all_distances(2)
# 6 6 12

g4 = Graph(5)
e4 = [(1, 2), (1, 3), (4, 2), (4, 5), (5, 3)]
for x, y in e4:
	g4.connect(x, y)
g4.find_all_distances(1)	
# 6 6 12 12
