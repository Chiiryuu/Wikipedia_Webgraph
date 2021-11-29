import pywikibot
import json
import sys


knownPages = []
pagesQueue = []
site = pywikibot.Site("en", "wikipedia")
nodeDictionary = {}

args = sys.argv[1:]

if len(args) < 1:
    print('Usage: python .\continue {Maximum depth (-1 for no limit)}\nHalt process and save with Ctrl+C.')
    exit(-1)

maxDepth = args[0]

try:
    maxDepth = int(maxDepth)
except:
    print("Invalid depth given.")
    print('Usage: python .\continue {Maximum depth (-1 for no limit)}\nHalt process and save with Ctrl+C.')
    exit(-1)

# Re-read categories file to find known nodes
knownNodeFile = open('categories.csv','r')
for line in knownNodeFile:
    nodeName = line.split(':')[0]
    knownPages.append(knownNodeFile)
knownNodeFile.close()


uncompletedNodeFile = open('UncompletedNodes.csv','r')
for line in uncompletedNodeFile:
    nodeName, depth = line.split(':')
    depth = int(depth)
    knownPages.append(nodeName)
    pagesQueue.append((nodeName,depth))
uncompletedNodeFile.close()



print("Querying Wikipedia...")

curDepth = -1


try:
    while len(pagesQueue) > 0:
        pageName, pageDepth = pagesQueue.pop(0)
        if (maxDepth > -1 and pageDepth > maxDepth):
            print("Max breadth depth reached!")
            break
        
        if (pageDepth > curDepth):
            curDepth += 1
            print("Current Depth:",curDepth)
        pageEdges = []
        page = pywikibot.Page(site, pageName)
        pages = page.linkedPages()
        
        pageCategories = open("categories.csv", 'a')
        categories = page.categories()
        categoryString = "{}:".format(pageName)
        for category in categories:
            categoryString+="{},".format(str(category).replace(',','')[14:-2])
        pageCategories.write(categoryString[:-1]+'\n')
        pageCategories.close()
        
        graph = open("Graph.csv", 'a')
        for relatedPage in pages:
            newPage = relatedPage.title()
            if (':' in newPage):
                continue
            if not newPage in knownPages:
                knownPages.append(newPage)
                pagesQueue.append((newPage,pageDepth+1))
            graph.write("{}:{}:{}\n".format(pageName,newPage, pageDepth+1))
        graph.close()
        
        
except KeyboardInterrupt:
        print("Keyboard interrupt called. Ending processing.")
except:
    print("Error processing node")
    
with open("UncompletedNodes.csv", 'w') as file:
    for element in pagesQueue:
        file.write("{}:{}\n".format(element[0],element[1]))
    file.close()

print("Production Completed")



