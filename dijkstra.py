#!/usr/bin/python3

from Graph import Graph
from Vertex import Vertex
from PriorityQueue import PriorityQueue


def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    print(pq.heapArray)
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                # This method is used when the distance to a vertex that is already in the queue is reduced,
                # and thus moves that vertex toward the front of the queue.
                pq.decreaseKey(nextVert,newDist)


def traverse(y):
    x = y
    while (x.getPred()):
        print(x.key)
        x = x.getPred()
    print(x.key)


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
    print("({}, distance {} )".format(v, v.getDistance()))
    for w in v.getConnections():
       print("({} -> {}, weight {})".format(v.key, w.key, v.getWeight(w)))

dijkstra(g,g.get_vertex("u"))

for v in g:
    print("({}, distance {} )".format(v, v.getDistance()))
    for w in v.getConnections():
        print("({} -> {}, weight {})".format(v.key, w.key, v.getWeight(w)))


traverse(g.get_vertex('z'))

