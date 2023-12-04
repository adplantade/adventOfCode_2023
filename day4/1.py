with open("input.txt") as fichier:
	total = 0
	for ligne in fichier.readlines():
		points = 0
		tab = [i.split(" ") for i in ligne.replace("  "," ").strip().split(":")[1].split("|")]
		for gagnant in tab[0]:
			if gagnant != "" and gagnant in tab[1]:
				if points == 0:
					points += 1
				else:
					points *=2
		total += points
	print(total)

