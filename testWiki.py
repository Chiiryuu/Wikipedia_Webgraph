import pywikibot
from pywikibot import textlib
import json
import sys



site = pywikibot.Site("en", "wikipedia")

page = pywikibot.Page(site, "Cat")
pageLinks = pywikibot.link_regex.finditer(textlib.removeDisabledParts(page.text))

for linkmatch in pageLinks:
    linktitle = linkmatch.group('title')
    if not ':' in linktitle:
        if '#' in linktitle:
            linktitle = linktitle[:linktitle.index('#')]
        print(linktitle)