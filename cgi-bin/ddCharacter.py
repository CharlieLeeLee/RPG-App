#!"C:\Python27\python.exe"

# Cross-Platform Character Sheet Web App
# Created by Charlie S. Norvell
# 9/14/2017


import Random

# A class specific to Dungeons & Dragons 5e characters
# Includes functions to do the math for character creation
# and leveling.
class DnDCharacter:

	def __init__(self, name):
		self.name = name
		self.abilities = [] 		# a blank array for ability scores
		self.feats = []				# a blank array for features
		self.languages = []			# language proficiencies
		self.weapons = []			# weapon proficiencies
		self.armor = []				# armor proficiencies
		self.tools = []				# tool proficiencies
		self.skills = [(0,0)]*18	# list of 18 tuples for skills the first number is the
									#	skill mod, while the second is whether or not the 
									#	character has proficiency
		self.HP = 0
		self.level = 1
		
	# random ability scores
	def randScores():
		def genScore():
			a = randint(1, 6)
			b = randint(1, 6)
			c = randint(1, 6)
			d = randint(1, 6)
			
			final = a + b + c + d - min(a, b, c, d)
			return final
		
		for i in range(0, 6):
			self.abilities[i] = genScore()
	
	# use the standard scores given in the Player's Handbook
	def standardScores():
		self.abilities[0] = 15
		self.abilities[1] = 14
		self.abilities[2] = 13
		self.abilities[3] = 12
		self.abilities[4] = 10
		self.abilities[5] = 8
	
	# manual ability score entry
	def manualScores(str, dex, con, int, wis, cha):
		self.abilities[0] = str
		self.abilities[1] = dex
		self.abilities[2] = con
		self.abilities[3] = int
		self.abilities[4] = wis
		self.abilities[5] = cha
	
	# switch scores to the right or left
	# dir = 0 for left, 1 for right
	# ability = index of the ability score you're moving
	def switchScore(dir, ability):
		if dir == 0:
			if ability == 0:
				helper = self.abilities[5]
				self.abilities[5] = self.abilities[0]
				self.abilities[0] = helper
			else:
				helper = self.abilities[ability - 1]
				self.abilities[ability-1] = self.abilities[ability]
				self.abilities[ability] = helper
		else:
			if ability == 5:
				helper = self.abilities[0]
				self.abilities[0] = self.abilities[5]
				self.abilities[5] = helper
			else:
				helper = self.abilities[ability + 1]
				self.abilities[ability + 1] = self.abilities[ability]
				self.abilities[ability] = helper
	
	
	# choose race, which affects ability scores, languages, proficiencies, and feats
	def chooseRace(race, subrace = None):
		self.race = race
		if race == "DRAGONBORN":
			self.abilities[0] += 2
			self.abilities[5] += 2
			self.size = "Medium"
			self.speed = 30
			self.feats.append("Draconic Ancestry")
			self.feats.append("Breath Weapon")
			self.feats.append("Damage Resistance")
			self.languages.append("Common", "Draconic")
		elif race == "DWARF":
			self.abilities[2] += 2
			self.size = "Medium"
			self.speed = 25
			self.feats.append("Darkvision 60ft.")
			self.feats.append("Dwarven Resilience", "Stone Cunning")
			self.weapons.append("Battleaxe", "handaxe", "light hammer", "warhammer")
			# addProficiency() choose smith's tools, brewer's supplies, or mason's tools
			self.languages.append("Common", "Dwarvish")
			if subrace == "HILL DWARF":
				self.abilities[4] += 1
				self.HP += self.level
			elif subrace = "MOUNTAIN DWARF":
				self.abilities[0] += 2
				self.armor.append("light", "medium")
		elif race == "ELF":
			self.abilities[1] += 2
			self.size = "Medium"
			self.speed = 30
			self.feats.append("Darkvision 60ft", "Fey Ancestry", "Trance")
			self.skills[11] = (0, 1)
			self.languages.append("Common", "Elvish")
			if subrace == "HIGH ELF":
				self.abilities[3] +=1
				self.weapons.append("longsword","shortsword","shortbow","longbow")
				#addSpell() one cantrip from the wizard spell list, INT is spellcasting ability
				#addLanguage() one extra language
			elif subrace == "WOOD ELF":
				self.abilities[4] +=1
				self.weapons.append("longsword","shortsword","shortbow","longbow")
				self.speed = 35
				self.feats.append("Mask of the Wild")
			elif subrace == "DROW":
				self.abilities[5] += 1
				self.feats.append("Darkvision 120ft")
				self.weapons.append("rapiers", "shortsword", "hand crossbow")
				self.feats.append("Sunlight Sensitivity", "Drow Magic")
		elif race == "GNOME":
			self.abilities[3] += 2
			self.size = "Small"
			self.speed = 25
			self.feats.append("Darkvision 60ft", "Gnome Cunning")
			self.languages.append("Common", "Gnomish")
			if subrace == "ROCK GNOME":
				self.abilities[2] +=1
				self.feats.append("Artificer's Lore", "Tinker")
			elif subrace == "FOREST GNOME":
				self.abilities[1] += 1
				#addSpell() minor illusion cantrip
				self.feats.append("Speak with Small Beasts")