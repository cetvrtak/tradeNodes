import re
from eu4_parser import parse

nodesFile = open('D:/source/repos/tradeNodes/00_tradenodes.txt')
rawNodes = parse(nodesFile)
nodesFile.close()

nodes = {}
currentNode = dict(location=-1, inland=False, outgoing=[])

for node in rawNodes:
	nodeName = node[0: node.find('=')]
	currentNode['location'] = re.search('location=([0-9]+)', node).group(1)
	if re.search('inland', node): currentNode['inland'] = True
	for outNode in re.findall('name=\"(\w+)', node):
		currentNode['outgoing'].append(outNode)

	nodes[nodeName] = currentNode
	currentNode = dict(location=-1, inland=False, outgoing=[])