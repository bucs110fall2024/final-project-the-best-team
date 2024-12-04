import pygame
import math
from src.player import Player
from src.arrow import Arrow
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Joe Mann the Bowman")
icon = pygame.image.load("assets/game_icon.png")
pygame.display.set_icon(icon)

#player
player = Player(300,300,45,"player_image.png")
player_image = pygame.image.load("assets/player_image.png")

#enemies
enemies = []#List of all enemies on screen
enemy_image = pygame.image.load("assets\enemy_image.png")
#arrows
arrows = [] #List of all arrows on screen
arrow_image = pygame.image.load("assets/arrow_image.png")
arrow_images = []


def on_screen(x,y):
    if((x<600 and x>0) and(y<600 and y>0)):
        return True
    return False


while True:
    screen.fill((0,128,0))
    player.turn()
    rotated_player_image = pygame.transform.rotate(player_image,player.angle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        keys = pygame.key.get_pressed()  # Checking pressed keys
        if keys[pygame.K_w]:
            player.move_up()
        elif keys[pygame.K_s]:
            player.move_down()
        elif keys[pygame.K_a]:
            player.move_left()
        elif keys[pygame.K_d]:
            player.move_right()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_e:
                arrows.append(Arrow(player.x,player.y,player.angle,"assets/arrow_image.png"))
                arrow_images.append(pygame.transform.rotate(arrow_image,arrows[len(arrows)-1].angle))
                print(arrows[0].angle,math.cos(arrows[0].angle*math.pi/180),math.sin((arrows[0].angle*math.pi/180)))


      #2. detect collisions and update models
    #Player model being updated
    #Enemy model being updated
    if(len(enemies)>0):
        j = len(enemies)#THESE VARIABLES HAVE VERY NONDESCRIPT NAMES. CHANGE LATER
        i = 0
        while (i<j): #This has to be a while loop because the range has to be able to change in the middle of the loop
            screen.blit(arrow_images[i],(arrows[i].x, arrows[i].y))

            if(on_screen(arrows[i].x,arrows[i].y)):
                arrows[i].move()
            else:
                arrows.pop(i)
                arrow_images.pop(i)
                i -= 1
                j -= 1
            i+=1
    #Arrow models being updated
    if(len(arrows)>0):
        j = len(arrows)#THESE VARIABLES HAVE VERY NONDESCRIPT NAMES. CHANGE LATER
        i = 0
        while (i<j): #This has to be a while loop because the range has to be able to change in the middle of the loop
            screen.blit(arrow_images[i],(arrows[i].x, arrows[i].y))

            if(on_screen(arrows[i].x,arrows[i].y)):
                arrows[i].move()
            else:
                arrows.pop(i)
                arrow_images.pop(i)
                i -= 1
                j -= 1
            i+=1
      #3. Redraw next frame
    screen.blit(rotated_player_image,(player.x,player.y))
      #4. Display next frame
    pygame.display.flip()

