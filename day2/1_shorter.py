import re
ROUGE_MAX = 12
VERT_MAX = 13
BLEU_MAX = 14

bonsIds = 0

with open("inputTronc.txt") as fichier:
	for ligne in fichier.readlines():
		rouges = max([int(i) for i in re.findall("(\d+) red", ligne)])
		verts = max([int(i) for i in re.findall("(\d+) green", ligne)])
		bleus = max([int(i) for i in re.findall("(\d+) blue", ligne)])
		t = re.findall("(?P<red> \d+) red.*(\d+) green", ligne)
		print()
		if rouges <= ROUGE_MAX and verts <= VERT_MAX and bleus <= BLEU_MAX:
			bonsIds += int(re.findall("Game (\d+):", ligne)[0])

	print(bonsIds)