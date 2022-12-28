import networkx as nx


def updateSize(filename, newSize):
    if(FS.nodes[filename]['parent'] == "/"):
        FS.nodes[FS.nodes[filename]['parent']]['size'] = FS.nodes[FS.nodes[filename]['parent']]['size'] + newSize
    else:
        FS.nodes[FS.nodes[filename]['parent']]['size'] = FS.nodes[FS.nodes[filename]['parent']]['size'] + newSize
        updateSize(FS.nodes[filename]['parent'], newSize)

INF = open("input.txt")
FS = nx.DiGraph()

FS.add_node("/", size=0, parent=None)
currentNode = "/"


for line in INF:
    parsed = line.strip().split(" ")
    if parsed[0] == "$":
        if parsed[1] == "cd":
            if parsed[2] == "..":
                if currentNode != "/":
                    currentNode = FS.nodes[currentNode]['parent']
            elif parsed[2] == "/":\
                currentNode = "/"
            else:
                nodeName = currentNode + parsed[2] + "/"
                currentNode = nodeName
    elif parsed[0] == "dir":
        nodeName = currentNode + parsed[1] + "/"
        if nodeName not in FS.adj[currentNode]:
            #first time encountering
            #add node
            FS.add_node(nodeName, parent=currentNode, size=0)

            #add edge
            FS.add_edge(currentNode, nodeName)
    else:
        # will just be a filesize
        nodeName = currentNode + parsed[1]
        if nodeName not in FS.adj[currentNode]:
            #first time encountering

            #add node
            FS.add_node(nodeName, parent=currentNode, size=parsed[0])

            #add edge
            FS.add_edge(currentNode, nodeName)

            #update size
            updateSize(nodeName, int(parsed[0]))



dirs = {}
for node in FS.nodes:
    if node[-1] == "/":
        if(FS.nodes[node]['size'] > 1272621):
            dirs[node] = FS.nodes[node]['size']

sorteddirs = sorted(dirs.items(), key=lambda x:x[1])
print(sorteddirs)




