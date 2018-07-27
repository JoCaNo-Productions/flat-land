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
        
        Ruin - 12m. removes all stacks of mark and and damages a 
        bonus 10 True Damage per stack, with in a medium Range.'''
        if self.mana < 12:
            self.game.alert('Not Enough Mana')
            return 1
        if self.cooldowns[1] > 0:
            self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
            return 2
        
        for x in self.marked:
            if abs(x.loc[0]-self.loc[0])<5 and abs(x.loc[1]-self.loc[1])<5:
                x.health-=self.marked[x]*10
                
        return 0
        

    def ability3(self):
        '''Bounty - 0m. passive. gain a bonus 5 Mana for ever 
        stack of mark on a player you kill. note Ruin uses up 
        marks so they can't be used to for bounty.'''
        
        #Note: can we have the Mark mod take care of this 
        #and also should we just return 0 for passives
        return 0

    def ult(self):
        '''DarkAtKnight.ult() -> None
        
        Ultimate: Shadow Walk - 50m. Become invisible and 
        becomes untargetable for the next 4 turns and if he 
        breaks his invisibility by attacking he gains double damage.'''
        if self.mana < 50:
            self.game.alert('Not Enough Mana')
            return 0
        if self.cooldowns[0] > 0:
            self.game.alert(f'{self.ability_names[0]} ability has not cooled down yet')
            return 2

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

