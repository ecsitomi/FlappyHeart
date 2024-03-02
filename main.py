#main.py
import pygame
from settings import *
from game import Game
                   
def main():
  pygame.init()
  pygame.mixer.init() 
  
  SCREEN = pygame.display.set_mode((0, 0), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN )  
  pygame.display.set_caption('Flappy Heart')
  clock = pygame.time.Clock()
  game = Game(SCREEN)
  starting = True 

  while True:
    if starting:
      game.starting()
    else:
      game.run()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
        elif event.key == pygame.K_SPACE:
          starting = False

    pygame.display.flip()
    clock.tick(FPS)

if __name__ == "__main__":
  main()