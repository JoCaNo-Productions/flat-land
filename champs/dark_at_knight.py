from base_classes import Champion
from mods import Mod, dot

class DarkAtKnight(Champion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mods['speed'].append(mark(self))
        self.direct = [0, 0]
        self.marked = defaultdict(int)
    
    def move(self, loc):
        self.direct = [self.loc[0]-loc[0], self.loc[1]-loc[1]]
        super().move(loc)

    def ability1(self) -> None:
        '''DarkAtKnight.ability1() -> None
        
        Mark - 5m. gain a bonus 3 attack and a bonus .1 movement speed
        towards a player, does stack. one turn cool down.'''
        target = self.game.selectplayer()
        if self.mana < 5:
            self.game.alert('Not Enough Mana')
            return 1
        if self.cooldowns[0] > 0:
            self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
            return 2
        if False: # Check for range
            self.game.alert("out of range")
            return 3 # Out of range return value
        if self.marked[target] >= 7:
            self.game.alert(f'Reached Cap of Marks on player {target.player.nick}')
            return 17
        self.mana -= 5
        self.marked[target] += 1
        self.cooldown[0] = 1
        return 0

    def ability2(self):
        '''DarkAtKnight.ability2() -> None
        
        Mark - 5m. gain a bonus 3 attack and a bonus .1 movement speed
        towards a player, does stack. one turn cool down.'''
        pass

    def ability3(self):
        '''DarkAtKnight.ability3() -> None
        
        Mark - 5m. gain a bonus 3 attack and a bonus .1 movement speed
        towards a player, does stack. one turn cool down.'''
        pass

    def ult(self):
        '''DarkAtKnight.ult() -> None
        
        Mark - 5m. gain a bonus 3 attack and a bonus .1 movement speed
        towards a player, does stack. one turn cool down.'''
        pass

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

def mark(cls): # Return Mod that handles ability 1 +speed +damage if direct is correct
    pass

def create(): # Return instance of DarkAtKnight, used by champion select
    return DarkAtKnight(**d)

