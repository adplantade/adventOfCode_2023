from string import digits

fichier = open("input.txt", "r")
total = 0
for ligne in fichier.readlines():
	chiffres = []
	for carac in ligne:
		if carac in digits:
			chiffres.append(carac)
	total += int(chiffres[0] + chiffres[-1])

print(total)