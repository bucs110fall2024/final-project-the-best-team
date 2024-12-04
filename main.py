import pygame
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

#arrows
arrows = [] #List of all arrows on screen

def on_screen(object):
    if(object.x<600 or object.x>0):
        return True
    if(object.y<600 or object.y>0):
        return True
    return False


while True:
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
            if event.type == pygame.K_e:
                arrows.append(Arrow(player.x,player.y,player.angle,"arrow_image.png"))
    screen.fill((0,128,0))


      #2. detect collisions and update models
    screen.blit(rotated_player_image,(player.x,player.y))
      #3. Redraw next frame

      #4. Display next frame
    pygame.display.flip()

