from edge import Edge, WeightedEdge
import pygame as pg
import random
import math
from WeightedGraph import WeightedGraph
pg.init()

class App:
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.screen = pg.display.set_mode((width,height))
		self.clock = pg.time.Clock()
		self.map = pg.image.load("USAMap.png")
	
	
	def fun(self,graph,t):
		if t == 1:
			for v in graph._vertices:
				v.pos = (random.randint(0,self.width/10),random.randint(0,self.height/10))
		else:
			for v in graph._vertices:
				n = random.randint(0,len(graph._vertices)-1)
				old = v.pos
				v.pos = graph._vertices[n].pos
				graph._vertices[n].pos = old
	
	def draw_graph(self,graph,path):
		'''
		for vertex in graph._vertices:
			pg.draw.circle(self.screen, (0,0,255), (vertex.pos[0]*self.width//100,vertex.pos[1]*self.height//100), 10)
			font = pg.font.SysFont('c059',self.width//100)
			f = font.render(vertex.name,False,(255,0,0))
			self.screen.blit(f,(vertex.pos[0]*(self.width/100),vertex.pos[1]*(self.height/100)+10))
		
		for ed in graph._edges:
			for edge in ed:
				f = graph._vertices[edge.u]
				s = graph._vertices[edge.v]
				col = (0,255,0)
				if f.name in path and s.name in path:
					if abs(path.index(f.name) - path.index(s.name))<=1:
						col = (255,0,0)
				pg.draw.line(self.screen,col,(f.pos[0]*(self.width/100),f.pos[1]*(self.height/100)),
							 (s.pos[0]*(self.width/100),s.pos[1]*(self.height/100)),3)'''
		for vertex in graph._vertices:
			pg.draw.circle(self.screen, (0,0,255), (vertex.pos[0]*self.width//100,vertex.pos[1]*self.height//100), 10)
			font = pg.font.SysFont('c059',self.width//100)
			f = font.render(vertex.name,False,(255,0,0))
			self.screen.blit(f,(vertex.pos[0]*(self.width/100),vertex.pos[1]*(self.height/100)+10))
		rr = []
		for ed in graph._edges:
			for edge in ed:
				f = graph._vertices[edge.u]
				s = graph._vertices[edge.v]
				col = (0,255,0)
				pg.draw.line(self.screen,(255,0,0),(f.pos[0]*(self.width/100),f.pos[1]*(self.height/100)),
							(s.pos[0]*(self.width/100),s.pos[1]*(self.height/100)),3)
		for edd in path:
			f = graph._vertices[edd.u]
			s = graph._vertices[edd.v]
			pg.draw.line(self.screen,(255,0,0),(f.pos[0]*(self.width/100),f.pos[1]*(self.height/100)),
						(s.pos[0]*(self.width/100),s.pos[1]*(self.height/100)),3)
	
	
	def set_pos111(self,graph,path):
		i = 0
		while True:
			if i >= len(graph._vertices):
				return graph
			
			self.screen.blit(self.map,(0,0))
			self.draw_graph(graph,path)
			pg.display.flip()
			self.clock.tick(30)
			self.screen.fill((0,0,0))
			
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
				if event.type == pg.MOUSEBUTTONDOWN:
					print(event.pos,graph._vertices[i])
					graph._vertices[i].pos = (event.pos[0]/(self.width/100),event.pos[1]/(self.height/100))
					i += 1
			
	
	
	
	def run(self,graph,path):
		#graph = self.set_pos(graph,path)
		num=''
		l = False
		mot = False
		point = 0
		
		while True:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
				if event.type == pg.KEYDOWN:
					num+=(pg.key.name(event.key))
				if event.type == pg.MOUSEBUTTONDOWN:
					for v in range(len(graph._vertices)-1):
						print(event.pos,graph._vertices[v].pos[0]*(self.width/100),graph._vertices[v].pos[1]*(self.height/100))
						if event.pos < (graph._vertices[v].pos[0]*(self.width/100)+10,graph._vertices[v].pos[1]*(self.height/100)+10):
							if event.pos > (graph._vertices[v].pos[0]*(self.width/100)-10,graph._vertices[v].pos[1]*(self.height/100)-10):
								mot = True
								point = v
								break
				if event.type == pg.MOUSEMOTION:
					if mot:
						graph._vertices[point].pos = (event.pos[0]/(self.width/100),event.pos[1]/(self.height/100))						
				if event.type == pg.MOUSEBUTTONUP:
					if mot:
						graph._vertices[point].pos = (event.pos[0]/(self.width/100),event.pos[1]/(self.height/100))
					point = 0
					mot = False
			
			if 'fun1' in num:
				num = ''
				l = not(l)
				t = 1
			elif 'fun2' in num:
				num = ''
				l = not(l)
				t=2
			
			if 'sc' in num or 'cs' in num:
				num=''
				self.map = pg.transform.scale(self.map, (random.randint(0,self.width),random.randint(0,self.height)))
			if 'nor' in num:
				num = ''
				self.map = pg.transform.scale(self.map, (self.width,self.height))
			
			if l:
				self.fun(graph,t)
			'''
			for e in graph._edges:
				graph.calc_distance(e)'''
			'''
			bfs_result = bfs("Washington",lambda x:x=="Phoenix",city_graph.neighbors_for_vertex)
			if bfs_result is None:
				print("no")
			else:
				solution = node_to_path(bfs_result)
			print(solution)'''

			
			self.screen.blit(self.map,(0,0))
			self.draw_graph(graph,path)
			pg.display.flip()
			self.clock.tick(30)
			self.screen.fill((0,0,0))


class Vertix:
	def __init__(self,name,pos):
		self.name = name
		self.pos = pos
		
	
	def __eq__(self,a):
		return self.name == a
	
	def __repr__(self):
		return self.name
	
	def __str__(self):
		return self.name
	
	def __hash__(self):
		return hash(self.name) ^ hash(self.pos)


class Graph:
	def __init__(self,vertices):
		self._vertices = vertices
		self._edges = [[] for _ in vertices]

	@property
	def vertex_count(self):
		return len(self._vertices)

	@property
	def edge_count(self):
		return len(self._edges)

	def add_vertex(self,vertex):
		self._vertixes.append(vertex)
		self._edges.append([])

	def add_edge(self,edge):
		self._edges[edge.u].append(edge)
		self._edges[edge.v].append(edge.reversed())

	def add_edge_by_indeces(self,u,v):
		edge = Edge(u,v)
		self.add_edge(edge)

	def add_edge_by_vertices(self,first,second):
		u = self._vertices.index(first)
		v = self._vertices.index(second)
		self.add_edge_by_indeces(u,v)

	def vertex_at(self,index):
		return self._vertices[index]

	def index_of(self,vertex):
		return self._vertices.index(vertex)

	def neighbors_for_index(self,index):
		return list(map(self.vertex_at,[e.v for e in self._edges[index]]))

	def neighbors_for_vertex(self,vertex):
		return self.neighbors_for_index(self._vertices.index(vertex))

	def edges_for_index(self,index):
		return self._edges[index]

	def edges_for_vertex(self,vertex):
		return self.edges_for_index(self.index_of(vertex))

	def __str__(self):
		desc = ""
		for i in range(self.vertex_count):
			print(desc,self.vertex_count,i)
			desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"

		return desc




if __name__ == "__main__":
		city_graph = WeightedGraph([Vertix("Seattle",(9,7)),Vertix("San Francisco",(3,38)),Vertix("Los Angeles",(8,51)),
		Vertix("Riverside",(13,51)),Vertix("Phoenix",(20,57)),Vertix("Chicago",(65,33))
		,Vertix("Boston",(94,25)),Vertix("New York",(89,30)),Vertix("Atlanta",(73,58))
		,Vertix("Miami",(84,82)),Vertix("Dallas",(49,63)),Vertix("Houston",(52,72)),
		Vertix("Washington",(85,37)),Vertix("Detroit",(73,30)),Vertix("Philadelphia",(87,34))])
		city_graph.add_edge_by_vertices("Seattle", "Chicago",1737)
		city_graph.add_edge_by_vertices("Seattle", "San Francisco",678)
		city_graph.add_edge_by_vertices("San Francisco", "Riverside",386)
		city_graph.add_edge_by_vertices("San Francisco", "Los Angeles",348)
		city_graph.add_edge_by_vertices("Los Angeles", "Riverside",50)
		city_graph.add_edge_by_vertices("Los Angeles", "Phoenix",357)
		city_graph.add_edge_by_vertices("Riverside", "Phoenix",307)
		city_graph.add_edge_by_vertices("Riverside", "Chicago",1704)
		city_graph.add_edge_by_vertices("Phoenix", "Dallas",887)
		city_graph.add_edge_by_vertices("Phoenix", "Houston",1015)
		city_graph.add_edge_by_vertices("Dallas", "Chicago",805)
		city_graph.add_edge_by_vertices("Dallas", "Atlanta",721)
		city_graph.add_edge_by_vertices("Dallas", "Houston",225)
		city_graph.add_edge_by_vertices("Houston", "Atlanta",702)
		city_graph.add_edge_by_vertices("Houston", "Miami",968)
		city_graph.add_edge_by_vertices("Atlanta", "Chicago",588)
		city_graph.add_edge_by_vertices("Atlanta", "Washington",543)
		city_graph.add_edge_by_vertices("Atlanta", "Miami",604)
		city_graph.add_edge_by_vertices("Miami", "Washington",923)
		city_graph.add_edge_by_vertices("Chicago", "Detroit",238)
		city_graph.add_edge_by_vertices("Detroit", "Boston",613)
		city_graph.add_edge_by_vertices("Detroit", "Washington",396)
		city_graph.add_edge_by_vertices("Detroit", "New York",482)
		city_graph.add_edge_by_vertices("Boston", "New York",190)
		city_graph.add_edge_by_vertices("New York", "Philadelphia",81)
		city_graph.add_edge_by_vertices("Philadelphia", "Washington",123)
		print(city_graph)

		from generic_search import astar,dfs,bfs,Node,node_to_path
		'''
		bfs_result = bfs("Washington",lambda x:x=="Riverside",city_graph.neighbors_for_vertex)
		if bfs_result is None:
			print("no")
		else:
			solution = node_to_path(bfs_result)
			print(solution)'''
		from mst import mst, total_score, print_weighted_path
		r = mst(city_graph,5)
		print_weighted_path(city_graph,r)
		
		app = App(1200,600)
		app.run(city_graph,r)
