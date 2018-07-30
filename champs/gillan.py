# Status: Needs Review and discussion (Caleb)

from base_classes import Champion
from mods import Mod, dot

class Gillan(Champion):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.player.inventory.append(Shield_Cons())
		self.abl3_active=False
		self.self.shield_feature=None
	
	def damage(self, amount:int, defend: bool=True, magic_attack: bool=False):
		if abl3_active==True:
			if defend==False:
				return FAILED_ATTACK
			else:
				return super().damage(amount= amount, defend=defend, magic_attack=magic_attack)
		else:
			return super().damage(amount= amount, defend=defend, magic_attack=magic_attack)

	def ability1(self) -> None:
		'''Gillan.ability1() -> None
		
		Charge: Gain a Bonus .5 decaying Movement Speed. 5m'''
		if self.mana < 5:
			self.game.alert('Not Enough Mana')
			return 1
		self.mana -= 5
		self.mods['speed'].append(charge_mod(self))
		return 0

	def ability2(self):
		'''Gillan.ability2() -> None
		
		Drop Shield: Leaves a "Shield" Terrain Were Gillan Was standing.
		Gillan Can not Use Shield of Strength until retrieving his shield.
		gain a bonus 1.2 movement speed but loses all Defense. 0m'''
		
		shield=False
		for x in self.player.inventory:
			if x.nick=='Shield_Cons':
				shield=True
		
		if shield ==False:
			self.game.alert('No shield')
			return 17
		
		self.shield_feature=Shield_Feat(self.pos)
		# ISSUE: We need to work out how items work
		return 0
		

	def ability3(self):
		'''Gillan.ability3() -> None
		
		Shield of Strength: Ignore all True Damage Gained this turn. five turn cool down. 8m'''
		if self.mana < 8:
			self.game.alert('Not Enough Mana')
			return 1
		if self.cooldowns[0] > 10:
			self.game.alert(f'{self.ability_names[2]} ability has not cooled down yet')
			return 2
		self.mana -= 8
		self.cooldown[0] = 0
		self.abl3_active=True
		self.mods['health'].append(shield_of_strength_mod)
		return 0

	def ult(self):
		'''Gillan.ult() -> None
		
		Call of the Shield: Gillan can after Channeling
		(not Doing anything) for one turn, teleport back to
		his shield if it was dropped. 20m'''
		if self.mana < 20:
			self.game.alert('Not Enough Mana')
			return 1
		if self.shield_feature!=None
		self.mana -= 20
		self.channel(length=1,action=self.ability3_afterchanneling)
		return 0
	
	def ult_afterchanneling(self) -> None:
		'''Gillan._afterchanneling() -> None'''
		self.move(self.self.shield_feature.pos)

class Shield_Cons(Consumable):
	def __init__(self):
		self.defense = 10
		self.speed=-1.2
		self.nick='Shield_Cons'

class Shield_Feat(Feature):
	def __init__(self,pos):
		self.pos=pos
	
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
	assert isinstance(champ, Gillan), 'Attempt to add charge_mod Mod() to non-Gillan champ'
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

def shield_of_strength_mod(champ):
	assert isinstance(champ, Gillan), 'Attempt to add shield_of_strength_mod Mod() to non-Gillan champ'
	def next_turn():
		champ.abl3_active=False
	mod = Mod(priority=5,
			  turn=next_turn,
			  lifetime=1,
			  )
	return mod

	
	
def create(): # Return instance of classname, used by champion select
	return Gillan(**d)

