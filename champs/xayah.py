# Status: Defaults

from base_classes import Champion
from mods import Mod, dot

class xayah(Champion):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.target=[None,0] #champion,stacks of Boredom
		self.mods['attack'].append((boredom(self)))
	
	def move(self, loc):
		super().move(loc)

	def attack(self, champ):
		if self.target[0]!=champ:
				self.target=[champ,0]
		super().attack(loc)

	def ability1(self) -> None:
		'''xayah.ability1() -> None
		
		Boredom - Passive. Boredom: Every Attack against a player places
		 a stack of Boredom on them. Boredom Reduces Xayahs Attack
		 by two. Stacks are Removed Every time Xayah attacks a 
		 new player.'''
		return SUCCESS

	def ability2(self):
		'''xayah.ability2() -> None
		
		Throw Cow patties - 10m. Every player Moves 1 Away From xayah.
		 in a weird way'''
		if self.mana < 10:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		for champ in champion.champ:
			if champ.loc[0]>self.loc[0]:
				x=1
			else:
				x=-1
			if champ.loc[1]>self.loc[1]:
				y=1
			else:
				y=-1
			champ.move([champ.loc[0]+x, champ.loc[1]+y])
		self.mana -= 10
		return SUCCESS
		

	def ability3(self):
		'''xayah.ability3() -> None
		
		Lasso - 12m. A other Player Moves 1 Towards Xayah. Medium Range.'''
		target = self.game.selectplayer()
		if self.mana < 12:
			self.game.alert('Not Enough Mana')
			return INSUFF_MANA
		if self.cooldowns[0] > 2:
			self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		if self.distance(target.loc)>5: # Check for range
			self.game.alert("out of range")
			return OUT_OF_RANGE # Out of range return value
		self.mana -= 12
		self.cooldown[0] = 2
		return 0

	def ult(self):
		'''xayah.ult() -> None
		
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

def boredom(champ): # Return Mod that handles ability
	assert isinstance(champ, xayah),
		'Attempt to add boredom Mod() to non-xayah champ'
	def modify(x):
		target,stacks=champ.boredom
		champ.boredom[1]=stacks+1
		return x - stacks*2
	mod = Mod(
		priority = 5,
		mod = modify,
		lifetime = float('inf')
	)
	return mod
