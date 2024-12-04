import pygame
import math
class Player:
  
  def __init__(self,x,y,angle,image):
    self.x = x
    self.y = y
    self.angle = angle
    self.image = image
    self.rotated_image = image
    #setup pygame data
    
  def move_left(self):
    self.x -= 2
  def move_right(self):
    self.x += 2
  def move_up(self):
    self.y -= 2
  def move_down(self):
    self.y += 2
  def turn(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    radians = math.atan2((self.y-mouse_y),(mouse_x-self.x))
    self.angle = (radians * 180)/(math.pi)