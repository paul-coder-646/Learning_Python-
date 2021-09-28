import random

# this is our markov chain represenatation

# define the graph vertices
class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent = {} # Nodes that we have an edge to 
        self.neighbors = []
        self.neighbor_weights = []

    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    # .get(vertex, 0) means that we get the corresponding weight the given vertex 
    # and if its non existent, we default to it being 0 
    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        pass

    # initializes probability map. Defines the probability for the vertex 
    # of changing state to one neighbor or another neighbor
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbor_weights.append(weight)

    def next_word(self):
        # randomly select next word based on weights
        return random.choices(self.neighbors, weights=self.neighbor_weights, k=1)[0]
        


# this Graph consists of vertices
class Graph(object):
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        # return all possible words 
        # (the word is the key to the vertex object holding it)
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value] # Get the vertice belonging to a word

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
