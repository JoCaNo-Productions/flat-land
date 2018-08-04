from random import choice,randint
import time
from pathlib import Path
from uuid import uuid4
from math import ceil

from mods import Mod, no_regen
from constants import ABILITY_NOT_SET

class Champion:
	# Champion defaults
	cd = {
		'health':99, # Hit points
		'max_health':99, # Max health champion can regen
		'health_regen':9, # Rate of health regen
		'defense':3, # Defense against non-magic attacks
		'speed':1, # Movement speed
		'attack':12, # Damage of regular attacks
		'attack_range':1, # Range of regular attacks
		'mana':25, # Currency of magic attacks/abilities
		'max_mana':100, # Max mana champion can regen
		'mana_regen':7, # Regeneration of mana
		'magic_mod':1.0, # Multiplier of magic attacks
		'magic_resist':0.0, # Resistance to others' magic attacks
	}
	until_values = [
		'targetable', # Targetable by attacks and non-passive abilities
		'visible', # Visible by real-life players
		'attack', # Can use regular attacks
		'move', # Can move
		'health_regen', # Can apply health_regen to health
		'mana_regen', # Can apply mana_regen to mana
	]
	# Champion attributes
	attrs = list(cd.keys())
	champs = {}
	def __init__(self, game, player, **kwargs):
		self.name = kwargs.get('name', 'Champion')
		self.id = kwargs.get('id', uuid4())
		self.loc = kwargs.get('loc', (0,0)) # Location
		self.game = game
		self.player = player
		self.cooldowns = [0, 0, 0, 0] # Ability cooldowns
		self.ability_names = [None, None, None, None]
		for attr, val in self.__class__.cd.items():
			setattr(self, '_' + attr, kwargs.get(attr, val))
		# The directory of the image for the champion
		self.image_dir = kwargs.get('image_dir', Path.home())

		# Each list contains a number of Mod()s, aka buffs and nerfs
		self.mods = {
			attr:[] for attr in self.__class__.attrs
		}
		self.until = {
			until:0 for until in self.__class__.until_values
		}
		# "no_regen" mod for after attacks, special abilities, etc.
		self.mods['health_regen'].append(no_regen(self))
		self.__class__.champs[self.id] = self
	
	def distance(self, loc1, loc2=None) -> float:
		'''Champion.distance(loc1[, loc2]) -> float
		
		Return distance between two locations.
		"loc2" defaults to Champion.loc'''
		if loc2 is None:
			loc2 = self.loc
		return ((loc1[0]-loc2[0])**2 + (loc1[1]-loc2[1])**2)**0.5
	
	def move(self, loc):
		'''Champion.move(loc) -> None
		
		Moves champion to loc if valid. Raises Exception if illegal move.'''
		pass
		# Change: Check self.until_move
	
	def attack(self, champ):
		'''Champion.attack(champ) -> None
		
		Attacks champ if valid. Raises Exception if illegal attack.'''
		pass
		# Change: Check self.until_attack
 	
	def damage(self,
			   amount: int,
			   defend: bool=True,
			   magic_attack: bool=False) -> int: # Add handling of magic resistance
		'''Champion.damage(amount: int, defend: bool=True) -> int
		
		Damage the champion and return amount of True damage.
		if defend is False, do not apply defense multiplier.'''
		if defend:
			# Never prevent more than 75% of damage
			if self.defense < .75*amount:
				amount -= self.defense
			else:
				amount *= .25
		self.health -= round(amount)
		return round(amount)
	
	def end_of_turn(self) -> None:
		# Apply standard changes to health and mana.
		if self._health > self.max_health: # Decay extra health
			self.health -= ceil((self.max_health-self._health)/2)
		elif self.until['health_regen'] == 0: # Otherwise, regen
			self.health = min(self._health + self.health_regen, self.max_health)
		if self._mana > self.max_mana: # Decay extra mana
			self.mana -= ceil((self.max_mana-self._mana)/2)
		elif self.until['mana_regen'] == 0: # Otherwise, regen
			self.mana = min(self._mana + self.mana_regen, self.max_mana)
		# Update mods
		remove = []
		for attr_mods in self.mods:
			for mod in attr_mods:
				if mod.lifetime <= 0:
					remove.append((attr_mods, mod))
					mod.final_action(self)
					continue
				mod.lifetime -= 1
				mod.turn()
		for attr_mods, mod in remove:
			attr_mods.remove(mod)
		# Update untils
		for until in self.until.keys():
			if self.until[until] > 0:
				self.until[until] -= 1

	def killed(self, dead_champ):
		pass
	
	def channel(self, duration=1, action=None):
		'''when active the champ can't move, attack or use abilities like a stun but self inflicted.
		action is a function that is run after channeling is done'''
		pass
		# Issue: Needs Work (Caleb)
	
	def ability1(self,loc):
		#first abilaty will vary can be passive
		return ABILITY_NOT_SET
	
	def ability2(self,loc):
		#second abilaty will vary can be passive
		return ABILITY_NOT_SET
	
	def ability3(self,loc):
		#third abilaty will vary can be passive
		return ABILITY_NOT_SET

	def ult(self):
		#best abilaty
		return ABILITY_NOT_SET
	
	def __str__(self):
		return self.name 

	def __getattr__(self, attr):
		if attr not in self.__class__.attrs:
			return getattr(super(), attr)
		final = getattr(self, '_' + attr)
		for mod in sorted(self.mods[attr], key=lambda x:x.priority):
			final = mod.mod(final)
		return final

	def __setattr__(self, attr, val):
		if attr not in self.__class__.attrs:
			setattr(super(), attr, val)
		setattr(self, '_' + attr, val)


class Consumable:
	pass


class Feature:
	pass


class Player:
	def __init__(self, nick, game, inven):
		self.nickname = nick
		self.game = game
		self.champ = None # Champion
		self.inventory = inven

	def setchamp(self, champ):
		pass


class Terrain:
	def __init__(self):
		self.name = ''
		self.speedmod = 1.0 # Speed Modifier -- float('inf') makes it impassable
		self.blocks_vision = False
		self.id = 0
	def act(self) -> None:
		'''Terrain.act() -> None
		
		Execute an action each turn.'''
		pass


class Game:
	def __init__(self):
		#map is a grid which is made of [terrainobj,playerobj]
		self.map = [
			[[None, None] for _ in range(9)] for _ in range(9)
		]
		#gets map type from user
		self.maptype=self.getmaptype()
		#fills the board with tiles per user request
		self.setupmap()
		#gets number of players
		self.numberofplayers = self.getplayernum()
		#get champion selection from players
		self.champions=self.championselect()
		#places players on the map
		self.placechamps()

	def main(self):
		pass

	def select_location(self):
		#get a location from user
		pass

	def select_player(self):
		pass
	
	def select_items(self, key=None):
		#gets a range of tiles from user
		pass

	def getmaptype(self):
		pass

	def setupmap(self):
		pass

	def getplayernum(self):
		pass

	def championselect(self):
		pass

	def placechamps(self):
		pass

