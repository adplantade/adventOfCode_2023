from alive_progress import alive_bar
MAXIMUM = 10**13

MAXIMUM = 100

class Truc:
	origine = 0 #le "quoi" qu'on donne
	destination = 0 #le "quoi" qu'on obtient
	portée = 0

	def __init__(self, destination, origine, portée) -> None:
		self.origine = int(origine)
		self.destination = int(destination)
		self.portée = int(portée)

	def __lt__(self, other):
		return self.destination < other.destination

	def __gt__(self, other):
		return self.destination > other.destination
	
	def __eq__(self, other):
		return self.destination == other.destination
	
	def étend(self, combien):
		"""
		@combien: valeur à connaitre (ex seed)
		@return: un int si la valeur est modifiée, False si non (ex soil)
		"""

		if self.origine + self.portée >= combien >= self.origine:
			return self.destination + (combien - self.origine)
		else:
			return False
	
	def __str__(self):
		return f"orig : {self.origine}, dest : {self.destination}, portée : {self.portée}"
	def __repr__(self):
		return self.__str__()

with open("D:\\projets_perso\\adventOfCode_2023\\day5\\ex.txt") as fichier:
	seed = []
	dico = {}
	mode = "seeds"
	print("LECTURE")
	with alive_bar(MAXIMUM) as bar: 
		for ligne in fichier.readlines():
			if ligne.startswith("seeds: "):
				seed = ligne.split()[1:]
			elif ligne.startswith("seed-to-soil map:"):
				mode = "soil"
			elif ligne.startswith("soil-to-fertilizer map:"):
				mode = "fertilizer"
			elif ligne.startswith("fertilizer-to-water map:"):
				mode = "water"
			elif ligne.startswith("water-to-light map:"):
				mode = "light"
			elif ligne.startswith("light-to-temperature map:"):
				mode = "temperature"
			elif ligne.startswith("temperature-to-humidity map:"):
				mode = "humidity"
			elif ligne.startswith("humidity-to-location map:"):
				mode = "location"
			elif ligne != "\n":
				if mode not in dico:
					print(mode)
					dico[mode] = []
				truc = Truc(ligne.split()[0],ligne.split()[1],ligne.split()[2])
				dico[mode].append(truc)
				# for i in range(truc.origine, truc.origine + truc.portée):
				# 	if truc.étend(i) == False:
				# 		print("AAAAAAAAAAAAAAAAAAAAAAAAA",mode,i)
				# 	else:
				# 		dico[mode][truc.étend(i)] = i
				# 	bar()
			bar()
	print("lu")

	lowest = -1
	print(dico)
	for gr in seed:
		last = int(gr)
		print(int(gr), end="")
		for k in list(dico.keys()):
			for i in dico[k]:
				if i.étend(last):
					last = i.étend(last)
			print("->" + str(last), end="")
		print()
		if last < lowest or lowest == -1:
			lowest = last
	print(lowest)
	# pour l'exemple, doit être 35

	
	# with alive_bar(MAXIMUM) as bar: 
	# 	for i in range(MAXIMUM):
	# 		dico["soil"][i] = i if not i in dico["soil"] else dico["soil"][i]
	# 		dico["fertilizer"][i] = i if not i in dico["fertilizer"] else dico["fertilizer"][i]
	# 		dico["water"][i] = i if not i in dico["water"] else dico["water"][i]
	# 		dico["light"][i] = i if not i in dico["light"] else dico["light"][i]
	# 		dico["temperature"][i] = i if not i in dico["temperature"] else dico["temperature"][i]
	# 		dico["humidity"][i] = i if not i in dico["humidity"] else dico["humidity"][i]
	# 		dico["location"][i] = i if not i in dico["location"] else dico["location"][i]
	# 		bar()
	# print("rempli")
	# lowest = -1
	# for gr in seed:
	# 	last = int(gr)
	# 	for k in list(dico.keys()):
	# 		last = dico[k][last]
	# 	if last < lowest or lowest == -1:
	# 		lowest = last
	# print(lowest)