from tkinter import *
from random import choice,randint
import time
from PIL import Image, ImageTk

class player:
  def __init__(self):
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
    self.magicresist=0
    self.mana
    self.poisined=0
    self.burned=0
    self.speed=0
    self.imagedir='C:\\'
    self.buffs=["health":0,
    	"atack":0,
        "atackdelay":0,
        "defence":0,
        "healthregen":0,
        "magicpower":0,
        "magicregen":0,
        "poisined":0,
        "burned":0,
        "speed":0]
    self.nerfs=["health":0,
    	"atack":0,        
        "atackdelay":0,
        "defence":0,
        "healthregen":0,
        "magicpower":0,
        "magicregen":0,
        "poisined":0,
        "burned":0,
        "speed":0]
  
  def checklength(self,loc1,loc2,length):
    pass
  
  def move(self,loc1,loc2):
    pass
  
  def atack(self,loc):
    pass
  
  def abilaity(self,loc):
    pass
  
  def selecttile(self):
    pass
  
  def selectrangeoftiles(self,size):
    pass
  
class terrain:
  def __init__(self):
    self.speedmod=0
    self.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    