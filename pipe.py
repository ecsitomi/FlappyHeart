import pygame
from settings import initialize

class Pipe():
  def __init__(self, color, y, speed):
    self.WIDTH, self.HEIGHT = initialize()
    self.surf = pygame.image.load(f'imgs/pipe/{color}/pipe.png').convert_alpha()
    self.rect = self.surf.get_rect(bottom=(WIDTH+100, HEIGHT+y))
    self.speed_y = speed
    self.speed_x = 6
    self.counter = 0

  def up_down(self):
    self.counter += 1
    if self.counter % 60 == 0:
      self.speed_y * (-1)
    self.rect.y += self.speed_y

  def run(self):
    self.up_down()
    self.rect.x -= self.speed_x