#main.py
import pygame, settings
from settings import *
from game import Game

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Flappy Heart')
WIDTH, HEIGHT = settings.initialize()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  
game = Game(SCREEN)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
          running = False  

  game.run()

  pygame.display.update()
  clock.tick(FPS)

pygame.quit()
