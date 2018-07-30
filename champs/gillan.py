# Status: Being Worked On (Caleb)

from base_classes import Champion
from mods import Mod, dot

class Gillan(Champion):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def move(self, loc):
		super().move(loc)

	def ability1(self) -> None:
		'''Gillan.ability1() -> None
		
		Charge: Gain a Bonus .5 decaying Movement Speed. 5m'''
		if self.mana < 5:
			self.game.alert('Not Enough Mana')
			return 1
		self.mana -= 5
		
		return 0

	def ability2(self):
		'''Gillan.ability2() -> None
		
		Name - 0m. Desc.'''
		target = self.game.selectplayer()
		if self.mana < 0:
			self.game.alert('Not Enough Mana')
			return 1
		if self.cooldowns[0] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return 2
		if False: # Check for range
			self.game.alert("out of range")
			return 3 # Out of range return value
		if False:
			self.game.alert(f'Reached Cap of ___ on player {target.player.nick}')
			return 4
		self.mana -= 0
		self.cooldown[0] = 0
		return 0
		

	def ability3(self):
		'''Gillan.ability3() -> None
		
		Name - 0m. Desc.'''
		target = self.game.selectplayer()
		if self.mana < 0:
			self.game.alert('Not Enough Mana')
			return 1
		if self.cooldowns[0] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return 2
		if False: # Check for range
			self.game.alert("out of range")
			return 3 # Out of range return value
		if False:
			self.game.alert(f'Reached Cap of ___ on player {target.player.nick}')
			return 4
		self.mana -= 0
		self.cooldown[0] = 0
		return 0

	def ult(self):
		'''Gillan.ult() -> None
		
		Name - 0m. Desc.'''
		target = self.game.selectplayer()
		if self.mana < 0:
			self.game.alert('Not Enough Mana')
			return 1
		if self.cooldowns[0] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return 2
		if False: # Check for range
			self.game.alert("out of range")
			return 3 # Out of range return value
		if False:
			self.game.alert(f'Reached Cap of ___ on player {target.player.nick}')
			return 4
		self.mana -= 0
		self.cooldown[0] = 0
		return 0

d = {
	'health':0,
	'max_health':0,
	'health_regen':0,
	'defense':0,
	'speed':0,
	'attack':0,
	'attack_range':0,
	'attack_delay':0,
	'mana':0,
	'max_mana':0,
	'mana_regen':0,
	'magic_mod':0,
	'magic_resist':0,
}

def charge_mod(champ): # Return Mod that handles ability
	assert isinstance(champ, DarkAtKnight), 'Attempt to add charge_mod Mod() to non-Gillan champ'
	start_speed = .5
	decrement=.1
	if start_damage%decrement != 0:
		raise Exception
	d = {'speed':start_damage}
	def modify(speed):
		return speed+d['speed']
	def next_turn():
		d['speed'] -= decrement
	mod = Mod(priority=5,
			  mod=modify,
			  turn=next_turn,
			  lifetime=start_speed//decrement,
			  )
	return mod


def create(): # Return instance of classname, used by champion select
	return classname(**d)

