#!/usr/bin/python3

from Graph import Graph
from Vertex import Vertex
from PriorityQueue import PriorityQueue


def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)



g = Graph()

g.add_vertex(Vertex("u"))
g.add_vertex(Vertex("v"))
g.add_vertex(Vertex("w"))
g.add_vertex(Vertex("x"))
g.add_vertex(Vertex("y"))
g.add_vertex(Vertex("z"))

for v in g:
    print(v)

g.add_edge("u","v",2)
g.add_edge("u","x",1)
g.add_edge("v","x",2)
g.add_edge("x","w",3)
g.add_edge("v","w",3)
g.add_edge("u","w",5)
g.add_edge("x","y",1)
g.add_edge("w","y",1)
g.add_edge("y","z",1)
g.add_edge("w","z",5)

for v in g:
    print(v)
    for w in v.getConnections():
        print("({} -> {}, weight {})".format(v.key, w.key, v.getWeight(w)))




dijkstra(g,g.get_vertex("u"))
