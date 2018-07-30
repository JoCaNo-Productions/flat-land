# Status: Being Worked On

from math import atan, cos, sin, pi
from collections import defaultdict

from base_classes import Champion
from mods import Mod, dot
from constants import *

class DarkAtKnight(Champion):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.name = 'Dark at Knight'
		self.mods['speed'].append(mark_speed(self))
		self.mods['attack'].append(mark_damage(self))
		self.direction = [0, 0]
		self.marked = defaultdict(int) # Players with marks
	
	def move(self, loc):
		self.direction = [self.loc[0]-loc[0], self.loc[1]-loc[1]]
		super().move(loc)

	def ability1(self) -> None:
		'''DarkAtKnight.ability1() -> None
		
		Mark - 5m. gain a bonus 3 attack and a bonus .1 movement speed
		towards a player, does stack. one turn cool down.'''
		target = self.game.selectplayer()
		if self.mana < 5:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[0] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		if False: # Check for range
			self.game.alert("Out of range")
			return OUT_OF_RANGE
		if self.marked[target] >= 7:
			self.game.alert(f'Reached Cap of Marks on player {target.player.nick}')
			return 101
		self.mana -= 5
		self.marked[target] += 1
		self.cooldown[0] = 1
		return SUCCESS

	def ability2(self):
		'''DarkAtKnight.ability2() -> None
		
		Ruin - 12m. removes all stacks of mark and and damages a 
		bonus 10 True Damage per stack, within a medium Range.'''
		if self.mana < 12:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[1] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		if False: # Check for range
			self.game.alert("Out of range")
			return OUT_OF_RANGE
		self.mana -= 12
		self.cooldowns[1] = 0 # ISSUE: What should this be?
		for target in self.marked:
			if self.distance(target) <= 5: # ISSUE: Is range 4 or 5?
				# Apply True damage
				target.damage(self.marked[target]*10, defend=False)
				# ISSUE: Remove marks if target out of range?
				# don't forget to remove marks from players
		return SUCCESS

	def ability3(self):
		'''DarkAtKnight.ability3() -> None
		
		Bounty - 0m. passive. gain a bonus 5 Mana for ever 
		stack of mark on a player you kill. note Ruin uses up 
		marks so they can't be used to for bounty.'''
		return PASSIVE
		# ISSUE: Implement this in self.kill()

	def ult(self):
		'''DarkAtKnight.ult() -> None
		
		Ultimate: Shadow Walk - 50m. Become invisible and 
		becomes untargetable for the next 4 turns and if he 
		breaks his invisibility by attacking he gains double damage.'''
		if self.mana < 50:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[0] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		# ISSUE: Not implemented yet

def within_direction(source, target, direct):
	'''within_direction(source, target, direct) -> bool
	
	Return True if target within 45 degrees of direct(ion) vector
	from source'''
	#import pdb; from math import atan, tan, sin, cos; pdb.set_trace()
	# -pi/2 <= angle_of_direct <= 3pi/2
	angle = atan(direct[0]/direct[1]) + pi*(direct[0]<0)
	# Unit vestors 45 degrees to the left and right of dir
	a = cos(angle + pi/4), sin(angle + pi/4)
	b = cos(angle - pi/4), sin(angle - pi/4)
	# Difference of position
	diff = target[0]-source[0], target[1]-source[1]
	if 0 in a: # Avoid division by zero if a is vertical or horizontal
		return direct[0]*diff[0] > 0 and direct[1]*diff[1] > 0
	# Vertical displacement of target from a and b
	target_a = (diff[0])/a[0]*a[1] - diff[1]
	target_b = (diff[0])/b[0]*b[1] - diff[1]
	# Vertical displacement of direct from a and b
	direct_a = (direct[0])/a[0]*a[1] - direct[1]
	direct_b = (direct[0])/b[0]*b[1] - direct[1]
	return target_a*direct_a > 0 and target_b*direct_b > 0
	
	

def mark_speed(champ):
	assert isinstance(champ, DarkAtKnight), 'Attempt to add mark_speed Mod() to non-DarkAtKnight champ'
	def modify(x):
		increment = 0
		for target, marks in champ.marked.items():
			if within_direction(champ.loc, target.loc, champ.direction):
				increment += marks
		return x + increment*0.1
	mod = Mod(
		priority = 5,
		mod = modify,
		lifetime = float('inf')
	)
	return mod

def mark_damage(champ):
	assert isinstance(champ, DarkAtKnight), 'Attempt to add mark_damage Mod() to non-DarkAtKnight champ'
	def modify(x):
		increment = 0
		for target, marks in champ.marked.items():
			if within_direction(champ.loc, target.loc, champ.direction):
				increment += marks
		return x + increment*3
	mod = Mod(
		priority = 5,
		mod = modify,
		lifetime = float('inf')
	)
	return mod


d = {
	'health':300,
	'max_health':300,
	'health_regen':3,
	'defense':0,
	'speed':3.3,
	'attack':50,
	'attack_range':1,
	'attack_delay':0,
	'mana':0,
	'max_mana':50,
	'mana_regen':4.5,
	'magic_mod':1.0,
	'magic_resist':0.0,
}

def create(): # Return instance of DarkAtKnight, used by champion select
	return DarkAtKnight(**d)

