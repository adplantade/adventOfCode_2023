class Carte:
	numero = 0
	gagnants = 0

	def __init__(self, numero):
		self.numero = numero

	def __eq__(self, other):
		return self.numero == other.numero
	def __str__(self):
		return f"Carte {self.numero}, {self.gagnants} gagnants"
	def __repr__(self) -> str:
		return self.__str__()


with open("input.txt") as fichier:
	total = 0
	tabCartes: list[Carte] = []
	for ligne in fichier.readlines():
		ligne = ligne.replace("  "," ").strip().split(":")
		carte = Carte(ligne[0])
		tab = [i.split(" ") for i in ligne[1].split("|")]
		for gagnant in tab[0]:
			if gagnant != "" and gagnant in tab[1]:
				carte.gagnants += 1
		tabCartes.append(carte)
	
	tabNombre = [1 for i in range(len(tabCartes))]
	for index, carte in enumerate(tabCartes):
		for i in range(carte.gagnants):
			try:
				tabNombre[index+i+1] += tabNombre[index]
			except:
				pass
	print(tabNombre, sum(tabNombre))

