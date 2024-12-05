import pygame
import math
class Enemy:
  
    def __init__(self,x,y,angle,image):
        self.x = x
        self.y = y
        self.angle = angle
        self.image = image
        #setup pygame data
    def move(self,player_x,player_y): 
      radians = math.atan2((self.y-player_y),(player_x-self.x))
      self.angle = (radians * 180)/(math.pi)
      if(player_x>self.x):
         self.x += 0.1
      else:
         self.x -= 0.1
      if(player_y>self.y):
         self.y += 0.1
      else:
         self.y -= 0.1