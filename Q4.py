from collections import defaultdict
class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)
		self.Time = 0

	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def findArticulationPoint(self, curr, visited, artPoint, parent, low, discovery):

		children = 0
		visited[curr]= True
		discovery[curr] = self.Time
		low[curr] = self.Time
		self.Time += 1

		for v in self.graph[curr]:
			if visited[v] == False :
				parent[v] = curr
				children += 1
				self.findArticulationPoint(v, visited, artPoint, parent, low, discovery)
				low[curr] = min(low[curr], low[v])
				if parent[curr] == -1 and children > 1:
					artPoint[curr] = True
				if parent[curr] != -1 and low[v] >= discovery[curr]:
					artPoint[curr] = True
					 
			elif v != parent[curr]:
				low[curr] = min(low[curr], discovery[v])
	
	def getArticulationPoint(self):
		self.time = 0

		visited = [False] * (self.V)
		discovery = [float("Inf")] * (self.V)
		low = [float("Inf")] * (self.V)
		parent = [-1] * (self.V)
		artPoint = [False] * (self.V) 

		for i in range(self.V):
			if visited[i] == False:
				self.findArticulationPoint(i, visited, artPoint, parent, low, discovery)

		for index, value in enumerate (artPoint):
			if value == True: print (index,end=" ")

g = Graph(13)
g.addEdge(0, 1)
g.addEdge(0, 6)
g.addEdge(0, 2)
g.addEdge(0, 5)
g.addEdge(2, 6)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(6, 9)
g.addEdge(4, 6)
g.addEdge(9, 11)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(9, 10)
g.addEdge(9, 12)
g.addEdge(11, 12)

g = Graph(7) #4
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(2, 4)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(5, 6)

g = Graph(6) # 0, 1
g.addEdge(0, 1)
g.addEdge(0, 5)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(4, 3)

print ("\nArticulation points in GIven graph ")
g.getArticulationPoint()