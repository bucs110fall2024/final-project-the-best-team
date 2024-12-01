import pygame
import math
class Player:
  
  def __init__(self,x,y,angle,image):
    x.self = x
    y.self = y
    angle.self = angle
    image.self = image
    #setup pygame data
    
  def move_left(self):
    self.x -= 2
  def move_right(self):
    self.x += 2
  def move_up(self):
    self.y += 2
  def move_down(self):
    self.y -= 2
  def turn(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    self.angle = math.atan(math.abs(self.y-mouse_y)/math.abs(self.x-mouse_x))*(180/math.pi())
    if((mouse_y-self.y)<0 and (mouse_x-self.x)<0):
      self.angle = self.angle + 180
    elif((mouse_y-self.y)<0):
      self.angle = self.angle + 270
    elif((mouse_x-self.x)<0):
      self.angle = self.angle + 90
    
