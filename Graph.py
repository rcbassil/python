#!/usr/bin/python3

from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_key, to_key, weight=None):
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbor(
            self.vertices[to_key],
            weight
        )

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())