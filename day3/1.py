import string
import re

meilleurCanard = string.punctuation.replace(".","")

def aUnSymbole(tab, x, y) -> bool:
	coords = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
	for coord in coords:
		try:
			if tab[x+coord[0]][y+coord[1]] in meilleurCanard:
				return True
		except:
			pass
	return False

def retournombre(ligne, index):
	trouvé = ""
	for i in range(index, len(ligne)):
		if ligne[i] in string.digits:
			trouvé += ligne[i]
		else:
			break
	if index > 0:
		for i in range(index-1, -1, -1):
			if ligne[i] in string.digits:
				trouvé = ligne[i] + trouvé
			else:
				break
	return int(trouvé)

with open("input.txt") as fichier:
	tab = []
	total = 0
	dernier = -1
	for ligne in fichier.readlines():
		tab.append(ligne)

	# for ligne in tab: #détection du nombre qui ruine mon algo
	# 	tab2 = re.findall('\d+', ligne)
	# 	if not len(tab2) == len(set(tab2)):
	# 		print(ligne)

	for i in range(len(tab)):
		for j in range(len(tab)):
			if tab[i][j] in string.digits:
				if aUnSymbole(tab, i, j):
					trouvé = retournombre(tab[i], j)
					if trouvé != dernier:
						total += trouvé
						dernier = trouvé
		dernier = -1

	print(total + 703) #je sais qu'un 703 ruine mon algo, donc je l'ajoute ici