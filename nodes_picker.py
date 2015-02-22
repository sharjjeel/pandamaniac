import sim
import sys
import json
import networkx
import random

filename = sys.argv[1]
num_players, num_seeds, unique_id, j= filename.split('.')

print(num_seeds)
implemented = False
G = networkx.Graph()
d = json.load(open(filename))

for a in d:
	for b in d[a]:
		G.add_edge(a, b)

if not implemented:
	output = 'upload.txt'
	f = open(output, 'w')
	nodes = G.nodes()
	for a in range(50):
		lst = []
		for b in range(int(num_seeds)):
			rc = random.choice(nodes)
			while rc in lst:
				rc = random.choice(nodes)
			lst.append(rc)
			f.write(rc+'\n')
	f.close()