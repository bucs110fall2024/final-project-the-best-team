import pygame
import math
class Player:
  
  def __init__(self,x,y,angle,image):
    self.x = x
    self.y = y
    self.angle = angle
    self.image = image
    self.rotated_image = image
    self.arrows = [0,0,0]
    self.arrowtype = 0
    #setup pygame data
    
  def move_left(self):
    if(self.x>0):
      self.x -= 5
  def move_right(self):
    if(self.x<550):
      self.x += 5
  def move_up(self):
    if(self.y>0):
      self.y -= 5
  def move_down(self):
    if(self.y<550):
      self.y += 5
  def turn(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    radians = math.atan2((self.y-mouse_y),(mouse_x-self.x))
    self.angle = (radians * 180)/(math.pi)