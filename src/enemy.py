import pygame
import math
class Enemy:
  
    def __init__(self,x,y,image):
        x.self = x
        y.self = y
        image.self = image
        #setup pygame data
    def move_to_player(self,player_x,player_y): 
        if(player_x>self.x):
           self.x += 1
        else:
           self.x -= 1
        if(player_y>self.y):
           self.y += 1
        else:
           self.y -= 1