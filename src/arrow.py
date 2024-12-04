import pygame
import math
class Arrow:
    def __init__(self,x,y,angle,image):
        self.x = x
        self.y = y
        self.angle = angle
        self.image = image
    def move(self):
        radians = (((self.angle)*math.pi)/180)
        self.y += math.sin(radians)*-1
        self.x += math.cos(radians)*1