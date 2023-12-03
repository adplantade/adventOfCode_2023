import string

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

def oùChiffres(tab, x, y) -> list:
	coords = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
	bonnes = []
	for coord in coords:
		try:
			if tab[x+coord[0]][y+coord[1]] in string.digits:
				bonnes.append((x+coord[0],y+coord[1]))
		except:
			pass
	return bonnes

with open("input.txt") as fichier:
	tab = []
	total = 0
	for ligne in fichier.readlines():
		tab.append(ligne)

	for i in range(len(tab)):
		for j in range(len(tab)):
			if tab[i][j] == "*":
				nbTrouvé = oùChiffres(tab, i, j)
				if len(nbTrouvé) >= 2:
					nomTrouvés = set()
					for coord in nbTrouvé:
						nomTrouvés.add(retournombre(tab[coord[0]], coord[1]))
					print(nomTrouvés)
					if len(nomTrouvés) == 2:
						total += nomTrouvés.pop() * nomTrouvés.pop()

	print(total)