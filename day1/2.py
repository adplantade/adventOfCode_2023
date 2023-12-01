from string import digits

fichier = open("input.txt", "r")
nombres = ["one","two","three","four","five","six","seven","eight","nine"]
total = 0
for ligne in fichier.readlines():
	premierPos = 999
	dernierPos = -2
	premier = ""
	dernier = ""
	for chiffre in range(0,9):
		ligne = ligne.replace(str(chiffre+1), nombres[chiffre])
	
	for chiffre in nombres:
		if ligne.find(chiffre) < premierPos and ligne.find(chiffre) != -1:
			premierPos = ligne.find(chiffre)
			premier = chiffre
		if ligne.rfind(chiffre) > dernierPos and ligne.rfind(chiffre) != -1:
			dernierPos = ligne.rfind(chiffre)
			dernier = chiffre

	total += (nombres.index(premier)+1) *10 + nombres.index(dernier) +1

print(total)