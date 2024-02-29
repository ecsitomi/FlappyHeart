#main.py
import pygame, settings
from settings import *
from game import Game
from scenes import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Flappy Heart')
WIDTH, HEIGHT = settings.initialize()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  
game = Game(SCREEN)
scenes = Scenes(SCREEN)

while starting:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      starting = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
          starting = False
      if event.key == pygame.K_SPACE:
        lighting(SCREEN, WHITE, 1000)
        starting = False
        running = True

  scenes.starting()

  pygame.display.update()
  clock.tick(FPS)
  
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
