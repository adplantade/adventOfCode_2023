import re
with open("input.txt") as fichier:
	tout = fichier.readlines()
	tps = re.findall(r"\d+", tout[0])
	dist = re.findall(r"\d+", tout[1])
	total = 0
	for clé, temps in enumerate(tps):
		distance = []
		for i in range(int(temps)):
			distance.append(i * (int(temps) - i))
		bons = [i for i in range(len(distance)) if distance[i] > int(dist[clé])]
		if (total == 0):
			total = 1
		total *= len(bons)
	print(total)