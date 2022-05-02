from mst import print_weighted_path
from WeightedGraph import WeightedGraph
from edge import WeightedEdge
from priority import PriorityQueue


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

class DijkstraNode:
	def __init__(self,vertex,distance):
		self.vertex = vertex
		self.distance = distance
	
	def __lt__(self,other):
		return self.distance < other.distance
	
	def __eq__(self,other):
		return self.distance == other.distance


def dijkstra(wg, root):
	first = wg.index_of(root)
	distances = [None] * wg.vertex_count
	distances[first] = 0
	path_dict = {}
	pq = PriorityQueue()
	pq.push(DijkstraNode(first,0))
	
	while not pq.empty:
		u = pq.pop().vertex
		dist_u = distances[u]
		for we in wg.edges_for_index(u):
			dist_v = distances[we.v]
			if dist_v is None or dist_v > we.weight + dist_u:
				distances[we.v] = we.weight + dist_u
				path_dict[we.v] = we
				pq.push(DijkstraNode(we.v, we.weight + dist_u))
	return distances, path_dict


def distance_array_to_vertex_dict(wg, distances):
	distance_dict = {}
	for i in range(len(distances)):
		distance_dict[wg.vertex_at(i)] = distances[i]
	return distance_dict

def path_dict_to_path(start,end,path_dict):
	if len(path_dict) == 0:
		return []
	edge_path = []
	e = path_dict[end]
	edge_path.append(e)
	while e.u != start:
		e = path_dict[e.u]
		edge_path.append(e)
	return list(reversed(edge_path))



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
		
		distances,path_dict = dijkstra(city_graph,"Los Angeles")
		name_distance = distance_array_to_vertex_dict(city_graph,distances)
		print("Distance from Los Angeles")
		for key, value in name_distance.items():
			print(f"{key}:{value}")
		print()
		print("The shortest path from Los Angeles to Boston")
		path = path_dict_to_path(city_graph.index_of("Los Angeles"),
		city_graph.index_of("Boston"),
		path_dict)
		print_weighted_path(city_graph,path)
