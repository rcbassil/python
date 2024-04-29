#!/usr/bin/python3

import sys

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        self.dist = sys.maxsize
        self.pred = None
        self.color = 'white'


    def add_neighbor(self, neighbor, weight=None):
        self.neighbors[neighbor] = weight

    def __str__(self):
        return '{} neighbors: {}'.format(
            self.key,
            [x.key for x in self.neighbors]
        )

    def getConnections(self):
        return self.neighbors.keys()

    def getWeight(self, neighbor):
        return self.neighbors[neighbor]
    
    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist
    
    def getColor(self):
        return self.color

    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setColor(self,color):
        self.color = color
