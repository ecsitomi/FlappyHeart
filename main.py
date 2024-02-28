import pygame, settings
from settings import *
from game import Game

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Flappy Heart')
WIDTH, HEIGHT = settings.initialize()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
bg_surf, bg_rect = settings.background(BG_IMG)
SCREEN.blit(bg_surf, bg_rect)
game = Game(SCREEN)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  game.run()

  pygame.display.update()
  clock.tick(FPS)
