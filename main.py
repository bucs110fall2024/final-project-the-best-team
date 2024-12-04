import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Joe Mann the Bowman")
icon = pygame.image.load("assets/game_icon.png")
pygame.display.set_icon(icon)
while True:
   x=1