import sys

# Remove program name from arguments
args = sys.argv[1:]

# If not enough arguments given, 
if len(args) < 3:
    print('Usage: python .\compress {Input File} {Output File} {Max Depth}')
    exit(-1)

# Get max depth from args
maxDepth = 0

inputFileName = args[0]
outputFileName = args[1]

try:
    maxDepth = int(args[2])
except:
    print('Usage: python .\compress {Input File} {Output File} {Max Depth}')
    exit(-1)

# Open original and compressed graph file
originalFile = open(inputFileName,'r')

newFile = open(outputFileName,'w')

print('Opening {} and finding nodes within max depth of {}.'.format(inputFileName, maxDepth))

# Iterate over graph file, writing nodes of depth < maxDepth to new file
for line in originalFile:
    if 'source:target:depth' in line:
        newFile.write(line)
        continue
    lineElements = line.split(':')
    depth = int(lineElements[2])
    if depth <= maxDepth:
        newFile.write(line)
originalFile.close()
newFile.close()


print('Original graph compressed to max depth {}, written to {}'.format(maxDepth, outputFileName))