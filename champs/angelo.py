# Status: Needs Review (Caleb)

from random import random

from base_classes import Champion
from mods import Mod, dot
from constants import *

class Angelo(Champion):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.tira_forte=0
		self.grey_health=0
		self.ult_active=False
	
	def damage(self, amount:int, defend: bool=True, magic_attack: bool=False)):
		health=self.health
		rtn_value=super().damage(amount= amount, defend=defend, magic_attack=magic_attack)
		damage=health-self.health
		self.grey_health+=damage
		return rtn_value
	
	def attack(champ):
		if super().attack(champ,attack=self.attack+self.tira_forte*15) == ATTACK_SUCCESSFUL:
			self.tira_forte=0
	
	def ability1(self) -> None:
		'''Angelo.ability1() -> None
		
		Lungo Shot - 20 Health every one range past 2.5 the following is 
		the chance of hitting 2.5/2.5, 2.5/3, 2.5/4, 2.5/5, ect. 15 True Damage.'''
		target = self.game.selectplayer()
		if self.health < 21:
			self.game.alert('Not Enough Health')
			return 17
		self.damage(amount=20,defend=False)
		distance=self.distance(self, target.loc)
		if distance<=2.5 or self.ult_active: #if player is close enough to have a guarantee Hit or ult_active
			target.damage(amount=15,defend=False)
			target.damage(amount=self.tira_forte*15,defend=True)
			# add tira_forte Damage without the true damage stat
			self.ult_active=False
		else: 
			chance= 2.5/distance #chance of hitting
			if random()>chance: 
				target.damage(amount=15,defend=False)
				target.damage(amount=self.tira_forte*15,defend=True)
			else:
				self.game.alert("Missed Lungo Shot")
		self.tira_forte=0	
		return 0

	def ability2(self) -> None:
		'''Angelo.ability2() -> None
		
		tira forte - 20 Health every time Angelo uses tira forte
		before he attacks he may add 15 damage to his attack.'''
		if self.health < 21:
			self.game.alert('Not Enough Health')
			return 17
		if tira_forte >5:
			self.game.alert(f'Reached Cap of tira forte on player {target.player.nick}')
			return 4
		self.damage(amount=20,defend=False)
		self.tira_forte+=1
		return 0

	def ability3(self) -> None:
		'''Angelo.ability3() -> None
		
		riposo - 0 health all damage done to Angelo including from abilities
		is kept in a stat called Grey health. Angelo may channel for one turn
		and then receive all grey health as health. ten turn cool down.'''
		if self.cooldowns[2] > 0:
			self.game.alert(f'{self.ability_names[2]} ability has not cooled down yet')
			return 2
		self.cooldown[0] = 11
		self.channel(length=1,action=self.ability3_afterchanneling)
		return 0
	
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
		if self.health < 201:
			self.game.alert('Not Enough Health')
			return 17
		self.damage(amount=200,defend=False)
		self.ult_active=True
		return 0

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

def create(): # Return instance of classname, used by champion select
	return Angelo(**d)
