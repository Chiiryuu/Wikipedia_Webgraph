import pywikibot
from pywikibot import textlib
import json
import sys


knownPages = []
pagesQueue = []
site = pywikibot.Site("en", "wikipedia")
nodeDictionary = {}


args = sys.argv[1:]

if len(args) < 3:
    print('Usage: python wiki.py {Output File Path} "{Starting Page Name}", {Maximum depth (-1 for no limit)}\nHalt process and save with Ctrl+C.')
    exit(-1)

filePath = args[0]
startingPage = args[1]
maxDepth = args[2]

try:
    maxDepth = int(maxDepth)
except:
    print("Invalid depth given.")
    print('Usage: python wiki.py {Output File Path} "{Starting Page Name}", {Maximum depth (-1 for no limit)}\nHalt process and save cut Ctrl+C.')
    exit(-1)

pagesQueue.append((startingPage,0))
knownPages.append(startingPage)


graph = open(filePath, 'w')
graph.write("source:target:depth\n")
graph.close()


pageCategories = open("categories-"+filePath, 'w')
pageCategories.close()

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
        
        # All page links, not just those in text
        '''
        page = pywikibot.Page(site, pageName)
        pages = page.linkedPages()
        
        pageCategories = open("categories-"+filePath, 'a')
        categories = page.categories()
        categoryString = "{}:".format(pageName)
        for category in categories:
            categoryString+="{},".format(str(category).replace(',','')[14:-2])
        pageCategories.write(categoryString[:-1]+'\n')
        pageCategories.close()
        
        graph = open(filePath, 'a')
        for relatedPage in pages:
            newPage = relatedPage.title()
            if (':' in newPage):
                continue
            if not newPage in knownPages:
                knownPages.append(newPage)
                pagesQueue.append((newPage,pageDepth+1))
            graph.write("{}:{}:{}\n".format(pageName,newPage, pageDepth+1))
        graph.close()
        '''
        
        # Updated version to just follow in-text links
        page = pywikibot.Page(site, pageName)
        pages = pywikibot.link_regex.finditer(textlib.removeDisabledParts(page.text))
        
        pageCategories = open("categories-"+filePath, 'a')
        categories = page.categories()
        categoryString = "{}:".format(pageName)
        for category in categories:
            categoryString+="{},".format(str(category).replace(',','')[14:-2])
        pageCategories.write(categoryString[:-1]+'\n')
        pageCategories.close()


        graph = open(filePath, 'a')
        for linkmatch in pages:
            newPage = linkmatch.group('title')
            if (':' in newPage):
                continue
            if '#' in newPage:
                newPage = newPage[:newPage.index('#')]
            if not newPage in knownPages and len(newPage) > 0:
                knownPages.append(newPage)
                pagesQueue.append((newPage,pageDepth+1))
            graph.write("{}:{}:{}\n".format(pageName,newPage, pageDepth+1))
        graph.close()
        
        
except KeyboardInterrupt:
        print("Keyboard interrupt called. Ending processing.")
except Exception as err:
    print("Error Encountered:\n",err)
    
with open("UncompletedNodes-"+filePath, 'w') as file:
    for element in pagesQueue:
        file.write("{}:{}\n".format(element[0],element[1]))
    file.close()

print("Production Completed")



