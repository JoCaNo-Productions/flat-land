from random import choice,randint
import time
from pathlib import Path

from mods import Mod

class Champion:
    # Champion defaults
    pd = {
        'health':100, # Hit points
        'max_health':100, # Max health champion can regen
        'health_regen':7, # Rate of health regen
        'defense':3, # Defense against non-magic attacks
        'dot':0, # Damage Over Time--applied each turn, decremented each time
        'burned':0, # Permanent damage you can not regen
        'speed':1, # Movement speed
        'attack':12, # Damage of regular attacks
        'attack_range':1, # Range of regular attacks
        'attack_delay':0, # Delay until regular attacks can be used again
        'mana':25, # Currency of magic attacks/abilities
        'max_mana':100, # Max mana champion can regen
        'mana_regen':7, # Regeneration of mana
        'magic_mod':1.0, # Multiplier of magic attacks
        'magic_resist':0.0, # Resistance to others' magic attacks
    }
    # Champion attributes
    attrs = list(pd.keys())
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Champion')
        self.id = kwargs.get('id', -1)
        self.loc = kwargs.get('loc', (0,0)) # Location
        for attr, val in self.__class__.pd.items():
            setattr(self, '_' + attr, kwargs.get(attr, val))
        # The directory of the image for the champion
        self.image_dir = kwargs.get('image_dir', Path.home())

        # Each list contains a number of Mod()s, aka buffs and nerfs
        self.mods = {
            attr:[] for attr in self.__class__.attrs
        }
    
    def distance(self, loc1, loc2=None):
        '''Champion.distance(loc1[, loc2]) -> distance between two locations
        
        loc2 defaults to Champion.loc'''
        if loc2 is None:
            loc2 = self.loc
        return ((loc1[0]-loc2[0])**2 + (loc1[1]-loc2[1])**2)**0.5
    
    def move(self, loc):
        '''Champion.move(loc) -> None
        
        Moves champion to loc if valid. Raises Exception if illegal move.'''
        pass
    
    def attack(self, loc):
        '''Champion.attack(loc) -> None
        
        Attacks space at loc if valid. Raises Exception if illegal attack.'''
        pass
    
    def ability1(self,loc):
        #first abilaty will vary can be passive
        pass
    
    def ability2(self,loc):
        #second abilaty will vary can be passive
        pass
    
    def ability3(self,loc):
        #third abilaty will vary can be passive
        pass

    def ult(self):
        #best abilaty
        pass
    
    def __str__(self):
        return self.name 

    def __getattr__(self, attr):
        if attr not in self.__class__.attrs:
            return getattr(super(), attr)
        final = getattr(self, '-' + attr)
        for mod in sorted(self.mods[attr], key=lambda x:x.priority):
            final = mod.mod(final)
        return final


class Player:
    def __init__(self, nick, champ):
        self.nickname = nick
        self.champ = champ # Champion


class Terrain:
    def __init__(self):
        self.name = ''
        self.speedmod = 1.0 # Speed Modifier -- float('inf') makes it impassable
        self.blocks_vision = False
        self.id = 0
    def act(self) -> None:
        '''Terrain.act() -> None
        
        Execute an action each turn.'''
        pass


class Game:
    def __init__(self):
        #map is a grid which is made of [terrainobj,playerobj]
        self.map = [
            [[None, None] for _ in range(9)] for _ in range(9)
        ]
        #gets map type from user
        self.maptype=self.getmaptype()
        #fills the board with tiles per user request
        self.setupmap()
        #gets number of players
        self.numberofplayers = self.getplayernum()
        #get champion selection from players
        self.champions=self.championselect()
        #places players on the map
        self.placechamps()

    def main(self):
        pass

    def selecttile(self):
        #get a tile from user
        pass
    
    def selectrangeoftiles(self,size):
        #gets a range of tiles from user
        pass

    def getmaptype(self):
        pass

    def setupmap(self):
        pass

    def getplayernum(self):
        pass

    def championselect(self):
        pass

    def placechamps(self):
        pass
