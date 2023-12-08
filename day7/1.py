from collections import Counter
ORDRE = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
RANGS = ["penta", "carré","full","brelan","double","paire","high"]

class Main:
	cartes = ""
	rang = ""
	mise = 0

	def __str__(self):
		return f"Cartes : {self.cartes}, {self.rang}, mise : {self.mise}"
	def __repr__(self):
		return self.__str__()
	def __gt__(self, other):
		if RANGS.index(self.rang) < RANGS.index(other.rang):
			return True
		elif (RANGS.index(self.rang) == RANGS.index(other.rang)):
			for i in range(len(self.cartes)):
				if ORDRE.index(self.cartes[i]) < ORDRE.index(other.cartes[i]):
					return True
		return False
	
	def __eq__(self, other):
		pass

with open("ex.txt") as fichier:
	tout = []
	mains = []
	for ligne in fichier.readlines():
		ligne = ligne.split()
		main = Main()
		main.cartes = ligne[0]
		elems = Counter(ligne[0]).most_common()
		if elems[0][1] == 5:
			main.rang= "penta"
		elif elems[0][1] == 4:
			main.rang = "carré"
		elif elems[0][1] == 3 and elems[1] == 2:
			main.rang = "full"
		elif elems[0][1] == 3:
			main.rang = "brelan"
		elif elems[0][1] == 2 and elems[1] == 2:
			main.rang = "double"
		elif elems[0][1] == 2:
			main.rang = "paire"
		else:
			main.rang = "high"

		mains.append(main)
	mains.sort()
	print(mains)