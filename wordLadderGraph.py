#!/usr/bin/python3

from Graph import Graph

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


myGraph = build_graph("wordfile.txt")
print(myGraph)

print(myGraph.get_vertices())

for v in myGraph:
    for w in v.get_connections():
        print("({} -> {})".format(v.key, w.key))
