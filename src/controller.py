from player import Player
import pygame
class controller: 
  def __init__(self):
   pygame.init()
   self.screen = pygame.display.set_mode(1000,1000)
   self.player = Player(500,500,45,"player.png")
   self.enemies = [Enemy(10,10,"enemy_image.png")]
   pygame.display.set_caption("Joe Mann the Bowman")
   icon = pygame.image.load("game_icon.png")
  def mainloop(self):
   """
   docstring
   """
   while(True):
      #1. Handle events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:
            self.player.move_up
          elif event.key == pygame.K_a:
            self.player.move_left
          elif event.key == pygame.K_s:
            self.player.move_down
          elif event.key == pygame.K_d:
            self.player.move_right



      #2. detect collisions and update models

      #3. Redraw next frame

      #4. Display next frame
      pygame.display.flip()
