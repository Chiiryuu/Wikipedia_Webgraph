# Wikipedia_Webgraph
An attempt to create a webgraph for wikipedia for a class project.

wiki.py: creates webgraph from specified starting page and maximum depth
  Usage: python .\wiki "{Starting Page Name}", {Maximum depth (-1 for no limit)}
  Halt process and save with Ctrl+C.
  
continue.py: After wiki.py is manually closed or exits due to network error, run this with specified depth to continue where it left off.
  Usage: python .\continue {Maximum depth (-1 for no limit)}
  Halt process and save with Ctrl+C.
  
graph.py: Explores created webgraph and can visualize relatively small webgraphs (size < 10,000)
  Usage: python .\graph.py
