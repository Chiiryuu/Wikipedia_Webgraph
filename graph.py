import matplotlib.pyplot as plt
import json
import io
import networkx as nx
import nxv

'''import networkx as nx
import matplotlib.pyplot as plt
import json
import io


file = io.open('GraphDic.json', mode="r", encoding="utf-8")
data = json.load(file)

#dic = json.loads(data)

G = nx.from_dict_of_lists(data)

#print(nx.convert.to_dict_of_lists(G))

nx.draw(G, with_labels = True)
plt.show()
'''


from matplotlib import pylab

def save_graph(graph,file_name):
    #initialze Figure
    plt.figure(num=None, figsize=(20, 20), dpi=80)
    plt.axis('off')
    fig = plt.figure(1)
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph,pos)
    nx.draw_networkx_edges(graph,pos)
    nx.draw_networkx_labels(graph,pos)

    '''
    cut = 1.00
    xmax = cut * max(xx for xx, yy in pos.values())
    ymax = cut * max(yy for xx, yy in pos.values())
    xmin = cut * min(xx for xx, yy in pos.values())
    ymin = cut * min(yy for xx, yy in pos.values())
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    '''
    plt.savefig(file_name,bbox_inches="tight")
    pylab.close()
    del fig


rawGraph = open('Graph.csv', "r")
next(rawGraph, None)
Graphtype = nx.Graph()

G = nx.parse_edgelist(rawGraph, delimiter=':', create_using=Graphtype,
                      nodetype=str, data=(('depth', int),))

print("Rendering Graph...")   

'''
style = nxv.Style(
    graph={"rankdir": "LR"},
    node=lambda u, d: {"shape": "circle" if u in "AEIOU" else "square"},
    edge=lambda u, v, d: {"style": "dashed", "label": u + v},
)
nxv.render(G, style, format="svg")
'''

#Assuming that the graph g has nodes and edges entered
save_graph(G,"wiki_graph.pdf")

#it can also be saved in .svg, .png. or .ps formats

print("Done!")