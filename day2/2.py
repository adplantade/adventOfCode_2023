import re

puissance = 0

with open("input.txt") as fichier:
	for ligne in fichier.readlines():
		rouge = max([int(i) for i in re.findall("(\d+) red", ligne)])
		vert = max([int(i) for i in re.findall("(\d+) green", ligne)])
		bleu = max([int(i) for i in re.findall("(\d+) blue", ligne)])

		puissance += (rouge * vert * bleu)


	print(puissance)