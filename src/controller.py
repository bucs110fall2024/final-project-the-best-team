import math
from src.player import Player
from src.enemy import Enemy
from src.arrow import Arrow
import pygame
class Controller: 
  def __init__(self):
    pygame.init()
    self.current_tick = 0
    #player
    self.player = Player(300,300,45,"player_image.png")
    self.player_image = pygame.image.load("assets/player_image.png")
    self.screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Joe Mann the Bowman")
    icon = pygame.image.load("assets/game_icon.png")
    pygame.display.set_icon(icon)
    #enemies
    self.enemies = []#List of all enemies on screen
    self.enemy_image = pygame.image.load("assets\enemy_image.png")
    #arrows
    self.arrows = [] #List of all arrows on screen
    self.arrow_image = pygame.image.load("assets/arrow_image.png")
    self.arrow_images = []
  def on_screen(self,x,y):
    if((x<600 and x>0) and(y<600 and y>0)):
        return True
    return False
  def detect_collision(self,collider,collided):
    if((collided.x+50>collider.x and collider.x>collided.x)and(collided.y+50>collider.y and collider.y>collided.y)):
        return True
    return False

  def mainloop(self):
    while True:
      self.screen.fill((0,128,0))
      self.current_tick+=1
      if self.current_tick==1000:
        self.enemies.append(Enemy(0,0,45,"enemy_image.png"))
        self.current_tick=0
        self.screen.fill((0,128,0))
      rotated_player_image = pygame.transform.rotate(self.player_image,self.player.angle)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        keys = pygame.key.get_pressed()  # Checking pressed keys
        if keys[pygame.K_w]:
          self.player.move_up()
        elif keys[pygame.K_s]:
          self.player.move_down()
        elif keys[pygame.K_a]:
          self.player.move_left()
        elif keys[pygame.K_d]:
          self.player.move_right()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_e:
            self.arrows.append(Arrow(self.player.x,self.player.y,self.player.angle,"assets/arrow_image.png"))
            self.arrow_images.append(pygame.transform.rotate(self.arrow_image,self.arrows[len(self.arrows)-1].angle))
#2. detect collisions and update models
        self.player.turn()
#Player model being updated
#Enemy model being updated
      if(self.enemies):
        j = len(self.enemies)#THESE VARIABLES HAVE VERY NONDESCRIPT NAMES. CHANGE LATER
        i = 0
        while (i<j): #This has to be a while loop because the range has to be able to change in the middle of the loop
          self.screen.blit(pygame.transform.rotate(self.enemy_image,self.enemies[i].angle),(self.enemies[i].x, self.enemies[i].y))
          self.enemies[i].move(self.player.x,self.player.y)
          l = len(self.arrows)
          k = 0
          while(k<l):
            if (self.enemies and (self.detect_collision(self.arrows[k],self.enemies[i]))):
              self.enemies.pop(i)
              self.arrows.pop(k)
              self.arrow_images.pop(k)
              k -= 1
              l -= 1
              i -= 1
              j -= 1
            k+=1
          i+=1
#Arrow models being updated
      ##print("Number of Arrows:",len(self.arrows))
      if(self.arrows):
        j = len(self.arrows)#THESE VARIABLES HAVE VERY NONDESCRIPT NAMES. CHANGE LATER
        i = 0
        while (i<j): #This has to be a while loop because the range has to be able to change in the middle of the loop
          self.screen.blit(self.arrow_images[i],(self.arrows[i].x, self.arrows[i].y))
          if(self.on_screen(self.arrows[i].x,self.arrows[i].y)):
            self.arrows[i].move()
          else:
            self.arrows.pop(i)
            self.arrow_images.pop(i)
            i -= 1
            j -= 1
          i+=1
#3. Redraw next frame
      self.screen.blit(rotated_player_image,(self.player.x,self.player.y))
#4. Display next frame
      pygame.display.flip()
 