from tkinter import *
from random import choice,randint
import time
from PIL import Image, ImageTk

class Player:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Player')
        self.id = kwargs.get('_id', -1)
        self.loc = kwargs.get('loc', (0,0)) # Location
        self.health = kwargs.get('health', 0)
        self.attack = kwargs.get('attack', 0)
        self.attack_delay = kwargs.get('attack_delay', 0)
        self.defence = kwargs.get('defence', 0)
        self.health_regen = kwargs.get('health_regen', 0)
        #a modifiyer for abilities
        self.magic_power = kwargs.get('magic_power', 0)
        self.magic_regen = kwargs.get('magic_regen')
        #a modifiyer for abilities
        self.magic_resist = kwargs.get('magic_resist', 0)
        self.mana = kwargs.get('mana', 0) # Currency of magic
        # DOT is decremented each turn after causing damage
        self.dot = kwargs.get('dot', 0) # Damage Over Time
        self.burned = kwargs.get('burned', 0) # Permanent damage
        self.speed = kwargs.get('speed', 0) # Movement speed
        #the directory of the image for the char
        self.imagedir='C:\\'

        self.buffs = [
            "health":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0 '''cycle length is in turns'''],
            "attack":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "attack_delay":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "defence":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "health_regen":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "magic_power":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "magic_regen":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "dot":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "burned":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "speed":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        ]

        self.nerfs = [
            "health":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "attack":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "attack_delay":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "defence":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "health_regen":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "magic_power":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "magic_regen":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "dot":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "burned":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
            "speed":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        ]
    
    def distance(self, loc1, loc2=None):
        '''Player.distance(loc1[, loc2]) -> distance between two locations
        
        loc2 defaults to Player.loc'''
        pass
    
    def move(self, loc):
        '''Player.move(loc) -> None
        
        Moves player to loc if valid. Raises Exception if illegal move.'''
        pass
    
    def attack(self, loc):
        '''Player.attack(loc) -> None
        
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


class terrain:
    def __init__(self):
        self.name = ''
        self.speedmod = 0.0 # Speed Modifier -- float('inf') makes it impassable
        self.blocks_vision = False
        self.id = 0

    def act(self) -> None:
        '''Terrain.act() -> None
        
        Execute an action each turn.'''
        pass

class game:
    def __init__(self):
        #map is a grid which is made of [terrainobj,playerobj]
        self.map=[[[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],
        [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],\
        [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],\
        [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],\
        [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],\
        [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],\
        [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],\
        [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]],\
        [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]]]
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



class GameGUI:
    def __init__(self):
        pass

class startscreenGUI:
    def __init__(self):
        pass

class numberofplayersGUI:
    def __init__(self):
        pass

class playerselectGUI:
    def __init__(self):
        pass

class mapselectorGUI:
    def __init__(self):
        pass

game=Game()
game.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
