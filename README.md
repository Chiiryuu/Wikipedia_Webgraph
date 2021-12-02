# Wikipedia_Webgraph
An attempt to create a webgraph for wikipedia for a class project.

wiki.py: creates webgraph from specified starting page and maximum depth
  Usage: python wiki.py "{Starting Page Name}", {Maximum depth (-1 for no limit)}
  Halt process and save with Ctrl+C.
  
continue.py: After wiki.py is manually closed or exits due to network error, run this with specified depth to continue where it left off.
  Usage: python continue.py {Maximum depth (-1 for no limit)}
  Halt process and save with Ctrl+C.
  
graphInfo.py: Explores created webgraph, printing info, and can visualize relatively small webgraphs (size < 10,000)
  Usage: python graph.py

compress.py: Compressed a generated webgraph to the provided breadth (etc from breadth 4 to 2)
  Usage: python compress.py {Input File} {Output File} {Max Depth}
