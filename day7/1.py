from collections import Counter
ORDRE = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
RANGS = ["penta", "carré","full","brelan","double","paire","high"]

class Main:
	cartes = ""
	rang = ""
	mise = 0
	place = 0

	def __str__(self):
		return f"Cartes : {self.cartes}, {self.rang}, mise : {self.mise}, place : {self.place}"
	def __repr__(self):
		return self.__str__()
	def __gt__(self, other):
		if RANGS.index(self.rang) < RANGS.index(other.rang):
			print(self.cartes,">", other.cartes," rang")
			return True
		elif (RANGS.index(self.rang) == RANGS.index(other.rang)):
			for i in range(len(self.cartes)):
				if ORDRE.index(self.cartes[i]) < ORDRE.index(other.cartes[i]):
					print(self.cartes,">",other.cartes," cartes", ORDRE.index(self.cartes[i]), ORDRE.index(other.cartes[i]))
					return True
				elif ORDRE.index(self.cartes[i]) > ORDRE.index(other.cartes[i]):
				    print(self.cartes[i],"<=",other.cartes[i])
				    return False
		print(self.cartes, "<", other.cartes, "fin")
		return False
	
	def __eq__(self, other):
		return Counter(self.cartes).most_common() == Counter(other.cartes).most_common()
		
	def __lt__(self, other):
	    if not self.__gt__(other) and not self.__eq__(other):
	        print(self.cartes,"<", other.cartes, "lower")
	        return True
	    return False

with open("input.txt") as fichier:
	mains = []
	for ligne in fichier.readlines():
		ligne = ligne.split()
		main = Main()
		main.cartes = ligne[0]
		main.mise = int(ligne[1])
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
	mains.sort(reverse=True)
	total =0
	for k, v in enumerate(mains):
	    total += v.mise * (len(mains) - k)
	    v.place = len(mains) - k
	
	print(mains)
	print(total)
	print(total == 6440)