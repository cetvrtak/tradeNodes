nodesFile = open('D:/Games/Europa Universalis IV v1.31.4/common/tradenodes/00_tradenodes.txt')
nodes = {}
currentNode = dict(location=-1, inland='no', outgoing=[])

for line in nodesFile:
	if line[0].isalnum():
		nodeName = line.split(sep="=")[0]
	if line.find('location') == 1:
		currentNode['location'] = line.split(sep="=")[1][0: -1]
	if line.find('inland') == 1:
		currentNode['inland'] = line.split(sep="=")[1][0: -1]
	if line.find('\tname') == 1:
		currentNode['outgoing'].append(line.split(sep="=")[1][1: -2])
	if line[0] == "}":
		nodes[nodeName] = currentNode
		currentNode = dict(location=-1, inland='no', outgoing=[])

nodesFile.close()

import pprint
pprint.pprint(nodes)