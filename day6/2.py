import re

with open("input.txt") as fichier:
	tout = fichier.readlines()
	tps = int("".join(re.findall(r"\d", tout[0])))
	dist = int("".join(re.findall(r"\d", tout[1])))
	print(len([i for i in range(tps) if (i * (tps - i)) > dist]))