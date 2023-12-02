import re

with open("input.txt") as fichier:
	total = 0
	for ligne in fichier.readlines():
		chiffres = re.findall("\d", ligne)
		total += int(chiffres[0] + chiffres[-1])
	print(total)