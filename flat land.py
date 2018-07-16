from tkinter import *
from random import choice,randint
import time
from PIL import Image, ImageTk

class player:
  def __init__(self):
  	#diplay name of player
  	self.name=''
  	#used my the game to interact with player
  	self.playerid=0
  	#location of tile which contains player
  	self.loc=[0,0]
    #an integer typicaly from 100-1000 at start
    self.health=0
    #when atacking subtract atack from health
    self.atack=0
    #a number typicaly 0 or 1 but can be longer
    #is the number of turns that must pass betwenn atacks
    self.atackdelay=0
    #the amount you subtrat from normal damage that you reseave to your health
    self.defence=0
    #the amount that you regen in a turn
    self.healthregen=0
    #a modifiyer for abilatys
    self.magicpower=0
    #a the amount that mana goes 
    self.magicregen=0
    #a modifiyer for abilatys
    self.magicresist=0
    #the currency for abilatys
    self.mana=0
    #the number of charges or poisin
    #every turn a charge will be removed along with a percent of health
    self.poisined=0
    #permanent damage
    self.burned=0
    #the amount of tiles player can move per turn
    self.speed=0
    #the director of the image for the char
    self.imagedir='C:\\'
    #positive efects 
    self.buffs=["health":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0 '''cycle length is in turns'''],
    	"atack":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "atackdelay":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "defence":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "healthregen":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "magicpower":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "magicregen":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "poisined":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "burned":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "speed":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0]]

    #negitive effects
    self.nerfs=["health":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
    	"atack":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],        
        "atackdelay":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "defence":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "healthregen":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "magicpower":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "magicregen":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "poisined":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "burned":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0],
        "speed":['amount':0,'forever':True,'amountremovedpercycle':.0,'cyclelength'0]]
  
  def checklength(self,loc1,loc2,length):
  	#checks if two locations are within the "length"
  	#returns true if within length
    pass
  
  def move(self,loc1,loc2):
  	#moves from loc1 to a loc2 after checking if legal
  	#returns true if legal
    pass
  
  def atack(self,loc):
  	#atacks loc after checking if in range
    pass
  
  def abilaity1(self,loc):
  	#first abilaty will vary can be passive
    pass
  
  def abilaity1(self,loc):
  	#first abilaty will vary can be passive
    pass
  
  def abilaity2(self,loc):
  	#second abilaty will vary can be passive
    pass
  
  def abilaity3(self,loc):
  	#third abilaty will vary can be passive
    pass

  def ult(self):
  	#best abilaty
  	pass

class terrain:
  def __init__(self):
    self.speedmod=0
    self.name=''
    self.impassible=False
    self.blocksvision=False
    self.id=0

  def action(self):
  	#an action that the tile preforms every turn
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


class MainGUI:
	def __init__(self):
		tk=Tk()

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
