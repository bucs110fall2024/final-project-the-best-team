import pygame
from src.player import Player
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Joe Mann the Bowman")
icon = pygame.image.load("assets/game_icon.png")
pygame.display.set_icon(icon)

player = Player(300,300,45,"player_image.png")
player_image = pygame.image.load("assets/player_image.png")

while True:
    player.turn()
    rotated_player_image = pygame.transform.rotate(player_image,player.angle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w:
            player.move_up()
          elif event.key == pygame.K_a:
            player.move_left()
          elif event.key == pygame.K_s:
            player.move_down()
          elif event.key == pygame.K_d:
            player.move_right()
    screen.fill((0,128,0))


      #2. detect collisions and update models
    screen.blit(rotated_player_image,(player.x,player.y))
      #3. Redraw next frame

      #4. Display next frame
    pygame.display.flip()
