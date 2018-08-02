# Status: Reviewed; Moving to finished champions

from random import random

from base_classes import Champion
from mods import Mod
from constants import *

class Angelo(Champion):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.name = 'Angelo'
		self.mods['attack'].append(tira_forte_attack(self))
		self.tira_forte=0
		self.grey_health=0
		self.ult_id =None
		self.ult_active=False
	
	def damage(self,
			   amount:int,
			   defend: bool=True,
			   magic_attack: bool=False) -> int:
		damage = super().damage(amount=amount, defend=defend, magic_attack=magic_attack)
		self.grey_health += damage
		return damage
	
	# ISSUE: Solidify if attack() returns SUCCESS or the amount of True damage
	def attack(champ):
		status = super().attack(champ)
		if status == SUCCESS:
			self.tira_forte = 0
	
	def ability1(self) -> None:
		'''Angelo.ability1() -> None
		
		Lungo Shot - 20 Health every one range past 2.5 the following is 
		the chance of hitting 2.5/2.5, 2.5/3, 2.5/4, 2.5/5, ect. 15 True Damage.'''
		target = self.game.selectplayer()
		if self.health <= 20:
			self.game.alert('Not Enough Health')
			return ANGELO_NOT_ENOUGH_HEALTH # ISSUE: Define this constant and import it
		self.damage(amount=20, defend=False)
		distance = self.distance(target.loc)
		# If player is close enough to have a guarantee Hit or ult_active
		if distance <= 2.5 or self.ult_active:
			# Apply 15 True damage and regular tira_forte damage
			target.damage(amount=15,defend=False)
			target.damage(amount=self.tira_forte*15,defend=True)
			self.ult_active=False
		else: 
			chance = 2.5/distance #chance of hitting
			if random() < chance:
				target.damage(amount=15,defend=False)
				target.damage(amount=self.tira_forte*15,defend=True)
			else:
				self.game.alert("Missed Lungo Shot")
		self.tira_forte=0
		return SUCCESS

	def ability2(self) -> None:
		'''Angelo.ability2() -> None
		
		tira forte - 20 Health every time Angelo uses tira forte
		before he attacks he may add 15 damage to his attack.'''
		if self.health <= 20:
			self.game.alert('Not Enough Health')
			return ANGELO_NOT_ENOUGH_HEALTH # ISSUE: Define and import
		if tira_forte >= 4:
			self.game.alert(f'Reached Cap of tira forte on player {target.player.nick}')
			return REACHED_CAP_STACKS
		self.damage(amount=20, defend=False)
		self.tira_forte+=1
		return SUCCESS

	def ability3(self) -> None:
		'''Angelo.ability3() -> None
		
		riposo - 0 health all damage done to Angelo including from abilities
		is kept in a stat called Grey health. Angelo may channel for one turn
		and then receive all grey health as health. ten turn cool down.'''
		if self.cooldowns[2] > 0:
			self.game.alert(f'{self.ability_names[2]} ability has not cooled down yet')
			return ABILITY_NOT_COOLED
		self.cooldowns[2] = 11
		self.channel(duration=1, action=self.ability3_afterchanneling)
		return SUCCESS
	
	def ability3_afterchanneling(self) -> None:
		'''Angelo.ability3_afterchanneling() -> None
		'''
		self.health+=self.grey_health
		self.grey_health=0
		if self.health>self.max_health:
			self.health=self.max_health

	def ult(self) -> None:
		'''Angelo.ult() -> None
		
		non è possibile - 200 health.  the next Lungo has inf range.'''
		if self.health <= 200:
			self.game.alert('Not Enough Health')
			return ANGELO_NOT_ENOUGH_HEALTH
		self.damage(amount=200, defend=False)
		self.ult_active=True
		return 0

def tira_forte_attack(champ):
	assert isinstance(champ, Angelo), 
		'Attempt to apply tira forte attack mod to non-Angelo champ'
	def modify(attack):
		return attack + champ.tira_forte*15
	mod = Mod(
		priority=32,
		mod=modify,
		liftime=float('inf'),
	)
	return mod

d = {
	'health':565,
	'max_health':565,
	'health_regen':10,
	'defense':5,
	'speed':2.7,
	'attack':20,
	'attack_range':2.5,
	'attack_delay':0,
	'mana':0,
	'max_mana':0,
	'mana_regen':0,
	'magic_mod':0,
	'magic_resist':0,
}

# Return instance of Angelo, used by champion select
def create():
	return Angelo(**d)
