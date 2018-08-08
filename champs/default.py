# Status: Defaults

from base_classes import Champion
from mods import Mod, dot
from constants import *

class classname(Champion):
	def __init__(self, game, player, **kwargs):
		super().__init__(game, player, **kwargs)
	
	def move(self, loc):
		super().move(loc)

	def ability1(self) -> int:
		'''classname.ability1() -> int
		
		Name - 0m. Desc.'''
		target = self.game.selectplayer()
		if self.mana < 0:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[0] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		if False: # Check for range
			self.game.alert("out of range")
			return OUT_OF_RANGE
		if False:
			self.game.alert(f'Reached Cap of ___ on player {target.player.nick}')
			return REACHED_CAP_STACKS
		self.mana -= 0
		self.cooldown[0] = 0
		return SUCCESS

	def ability2(self) -> int:
		'''classname.ability2() -> int
		
		Name - 0m. Desc.'''
		target = self.game.selectplayer()
		if self.mana < 0:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[1] > 0:
			self.game.alert(f'{self.ability_names[1]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		if False: # Check for range
			self.game.alert("out of range")
			return OUT_OF_RANGE
		if False:
			self.game.alert(f'Reached Cap of ___ on player {target.player.nick}')
			return REACHED_CAP_STACKS
		self.mana -= 0
		self.cooldown[1] = 0
		return SUCCESS
		

	def ability3(self) -> int:
		'''classname.ability3() -> int
		
		Name - 0m. Desc.'''
		target = self.game.selectplayer()
		if self.mana < 0:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[2] > 0:
			self.game.alert(f'{self.ability_names[2]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		if False: # Check for range
			self.game.alert("out of range")
			return OUT_OF_RANGE
		if False:
			self.game.alert(f'Reached Cap of ___ on player {target.player.nick}')
			return REACHED_CAP_STACKS
		self.mana -= 0
		self.cooldown[2] = 0
		return SUCCESS

	def ult(self) -> int:
		'''classname.ult() -> int
		
		Name - 0m. Desc.'''
		target = self.game.selectplayer()
		if self.mana < 0:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[3] > 0:
			self.game.alert(f'{self.ability_names[3]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		if False: # Check for range
			self.game.alert("out of range")
			return OUT_OF_RANGE
		if False:
			self.game.alert(f'Reached Cap of ___ on player {target.player.nick}')
			return REACHED_CAP_STACKS
		self.mana -= 0
		self.cooldown[3] = 0
		return SUCCESS

d = {
	'health':0,
	'max_health':0,
	'health_regen':0,
	'defense':0,
	'speed':0,
	'attack':0,
	'attack_range':0,
	'mana':0,
	'max_mana':0,
	'mana_regen':0,
	'magic_mod':0,
	'magic_resist':0,
}

def mod(var): # Return Mod that handles ability
	pass

def create(game, player): # Return instance of classname, used by champion select
	return classname(game, player, **d)
