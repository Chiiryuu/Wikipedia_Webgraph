import matplotlib.pyplot as plt
import json
import io
import networkx as nx
import sys


def printShortestPath(G, start, end):
    nodes = G.nodes()
    if not start in nodes:
        print("ERROR: node '{}' is not in graph!".format(start))
        return
    if not end in nodes:
        print("ERROR: node '{}' is not in graph!".format(end))
        return
    path = None
    try:
        path = nx.shortest_path(G, start, end)
    except nx.exception.NetworkXNoPath:
        print("No path fround between {} and {}.".format(start,end))
        return
    pathString = ' -> '.join(path)
    print("Shortest Path: {}\nPath length: {}".format(pathString,len(path)))
    return


    
    
args = sys.argv[1:]

# If not enough arguments given, 
if len(args) < 1:
    print('Usage: python shortestPath.py {Input File}')
    exit(-1)

graphFile = args[0]

print('Loading graph file {}...'.format(graphFile))

rawGraph = open(graphFile, "r")
next(rawGraph, None)
Graphtype = nx.DiGraph()

print('Converting graph file to Networkx Graph...')

G = nx.parse_edgelist(rawGraph, delimiter=':', create_using=Graphtype,
                      nodetype=str, data=(('depth', int),))
                      
                      
print('Loading complete!')

print('Use Ctrl+C to exit at anytime.')


try:
    while True:
        start = input("Enter starting page: ")
        end = input("Enter ending page: ")
        printShortestPath(G,start, end)
except exception as e:
    print("Program closing. Thanks for playing!\n",e)