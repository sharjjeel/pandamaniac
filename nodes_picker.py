import sim
import sys
import json
import networkx
import random
import collections

filename = sys.argv[1]
num_tries = int(sys.argv[2])
num_players, num_seeds, unique_id, j= filename.split('.')
num_seeds = int(num_seeds)

implemented = True
highest_degree = False
G = networkx.Graph()
d = json.load(open(filename))

for a in d:
	for b in d[a]:
		G.add_edge(a, b)

otpt_list = []

if not implemented:
	nodes = G.nodes()
	lst = []
	for b in range(int(num_seeds)):
		rc = random.choice(nodes)
		while rc in lst:
			rc = random.choice(nodes)
		lst.append(rc)
	otpt_list = otpt_list + lst
elif not highest_degree:
	degrees = G.degree(G.nodes())
	c = collections.Counter(degrees)
	bot_highest = c.most_common(num_seeds)
	half_of_bot = c.most_common(num_seeds/2)
	left_seeds = num_seeds - len(half_of_bot);
	for k, v in half_of_bot:
		otpt_list.append(k);
	bot_neighbors = []
	for k in otpt_list:
		bot_neighbors.append(G.neighbors(k))
	intersect = set.intersection(*map(set,d))

	intersect_not_top = []
	for a in intersect:
		if a not in bot_highest:
			intersect_not_top.append(a)

	if len(intersect_not_top) >= left_seeds:
		i = 0
		while left_seeds>0:
			otpt_list.append(intersect_not_top[i])
			i = i+1
			left_seeds = left_seeds - 1

	else:
		for i in intersect_not_top:
			otpt_list.append(i)
			left_seeds = left_seeds - 1
		highest_degree_plus_left_seeds = c.most_common(2*num_seeds)
		items = highest_degree_plus_left_seeds
		i = 0

		while left_seeds > 0:
			if items[num_seeds/2+ i][0] not in otpt_list:
				otpt_list.append(items[num_seeds/2+ i][0])
				i = i + 1
				left_seeds = left_seeds - 1
			else:
				i = i+1

output = 'upload.txt'
f = open(output, 'w')
nodes = G.nodes()
for a in range(num_tries):
	for b in otpt_list:
		f.write(b+'\n')
f.close()