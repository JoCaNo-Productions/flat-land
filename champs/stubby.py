# Status: Defaults

from base_classes import Champion
from mods import Mod, dot
from constants import *

class Stubby(Champion):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.name = 'Stubby'
		self.ability_names = []
		self.mods['speed'].append(vault_speed(self))

	
	def move(self, loc):
		super().move(loc)

	def ability1(self) -> int:
		'''Stubby.ability1() -> int
		
		Regular Swing - 5m. Attacks a player within 3 paces
		enflicting 55 damage. Recharges in two turns'''
		target = self.game.selectplayer()
		if self.mana < 5:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[0] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		if self.distance(target.loc) > 3:
			self.game.alert("out of range")
			return OUT_OF_RANGE
		self.mana -= 5
		self.cooldown[0] = 2
		target.damage(amount=55)
		return SUCCESS

	def ability2(self) -> int:
		'''Stubby.ability2() -> int
		
		Wide Swing - 7m. Attacks all players within 4 paces enflicting 45 damage.
		The wide swing throws Stubby off balance for one turn. Recharges in two turns.'''
		if self.mana < 7:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[1] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		self.mana -= 7
		self.cooldown[1] = 2
		for champ in self.__class__.champs:
			if self.distance(champ.loc) <= 4:
				champ.damage(amount=45)
		self.channel(duration=1)
		return SUCCESS
		

	def ability3(self) -> int:
		'''Stubby.ability3() -> int
		
		Vault - 12m. Use the hammer to vault a distance of four spaces (read description for how this is possible).
		Stubby must recover his composure and not move or attack after such an effort for one turn.
		Tile speed reductions are not applied (except impassable ones). Recharges in two turns.'''
		if self.mana < 12:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[2] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		self.mana -= 12
		self.cooldown[2] = 2
		self.vaulting = True # Apply vault_speed mod
		self.until['move'] = 0
		loc = self.game.select_location() # ISSUE: implement what range they select from
		#ISSUE: Check the selection to make sure there is no impassable terrain
		self.move(loc=loc, slow=False)
		self.vaulting = False
		self.channel(duration=1)
		return SUCCESS

	def ult(self) -> int:
		'''Stubby.ult() -> int
		
		Ultimate: Stubbed Toe - 30m. Stubby 'wills' a rock into being in front of any
		opponent he chooses anywhere on the map. As soon as the enemy moves, the enemy is
		unable to move the next turn and recieves a speed reduction the two turns after that.
		10 damage is inflicted with 5 health permanently burned on top of that. Recharges in six turns.'''
		if self.mana < 30:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[3] > 0:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		target = self.game.selectplayer()
		self.mana -= 30
		self.cooldown[3] = 6
		target.until['move'] += 1
		target.mods['speed'].append(ult_slow())
		target.damage(amount=10, defend=True)
		target.damage(amount=5, defend=False)
		return SUCCESS

d = {
	'health':875,
	'max_health':875,
	'health_regen':7,
	'defense':4,
	'speed':1.3,
	'attack':25,
	'attack_range':1,
	'mana':25,
	'max_mana':70,
	'mana_regen':3,
	'magic_mod':0,
	'magic_resist':0,
}

def vault_speed(champ):
	assert isinstance(champ, Stubby),
		'Attempt to add vault speed boast to non-Stubby champion'
	def modify(speed):
		if champ.vaulting:
			return speed + 2.7 # 1.3 + 2.7 == 4
		return speed
	mod = Mod(
		priority=5,
		mod=modify,
		lifetime=float('inf'),
	)
	return mod

def ult_slow():
	def modify(speed):
		return speed * 0.4
	mod = Mod(
		priority=32,
		mod=modify,
		lifetime=3,
	)
	return mod

def create(game, player): # Return instance of Stubby, used by champion select
	return Stubby(game, player, **d)
