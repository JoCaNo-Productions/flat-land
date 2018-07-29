from typing import Callable, Type, TypeVar
from uuid import uuid4

default = lambda *_: None

Player = TypeVar('Player')

class Mod:
	'''Mod()'s are used to add buffs or nerfs to Player()'s
	
	Note: this will change to a data class in the future'''
	def __init__(self,
				 id: int = None,
				 champ: Type[Player] = None,
				 priority: int = 20,
				 mod: Callable[[float], float] = default,
				 turn: Callable[[], None] = default,
				 lifetime: float = 0.0,
				 cycle: int = 1,
				 delay: int = 0,
				 last_action: Callable[[Type[Player]], None] = default,
				):
		self.id = id if id is not None else uuid4()
		self.champ = champ
		self.priority = priority # the closer to one, the sooner it is applied
		self.mod = mod
		self.turn = turn # A function called each turn
		self.lifetime = lifetime # number of turns until Mod() expires
		self.cycle = cycle # number of turns before cycling again
		self.delay = delay # number of turns until applied--reset to cycle when reaches 0
		self.last_action = last_action # called when lifetime reaches 0

def dot(start_damage, decrement=1):
	start_damage = abs(start_damage) # So there is no confusion of sign + or -
	if start_damage%decrement != 0:
		raise Exception
	d = {'damage':start_damage}
	def modify(health_regen):
		return -1 * d['damage']
	def next_turn():
		d['damage'] -= decrement
	mod = Mod(id=0,
			  priority=32, # Last modifier
			  mod=modify,
			  turn=next_turn,
			  lifetime=start_damage//decrement,
			  )
	return mod
