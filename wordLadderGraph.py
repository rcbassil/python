#!/usr/bin/python3

from Graph import Graph
from Queue import Queue
from Vertex import Vertex

def build_graph(word_file):
    d = {}
    g = Graph()
    wfile = open(word_file, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1] # removes the \n in the end of each word
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g


def bfs(start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.get_connections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')


def traverse(y):
    x = y
    while (x.getPred()):
        print(x.key)
        x = x.getPred()
    print(x.key)




myGraph = build_graph("wordfile.txt")
print(myGraph)

print(myGraph.get_vertices())

#for v in myGraph:
#    for w in v.get_connections():
#        print("({} -> {})".format(v.key, w.key))

print(myGraph.get_vertex('AAHS'))

bfs(myGraph.get_vertex('AAHS'))

for v in myGraph:
    for w in v.get_connections():
        print("({} -> {}, weight {}, dist {} , color {})".format(v.key, w.key, v.get_weight(w), v.getDistance(), v.getColor()))


traverse(myGraph.get_vertex('ACNE'))