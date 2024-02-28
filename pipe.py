#pipe.py
import pygame
from settings import initialize

class Pipe(pygame.sprite.Sprite):
  def __init__(self, color, y, speed_y, speed_x, invert):
    super().__init__()
    self.WIDTH, self.HEIGHT = initialize()
    self.image = pygame.image.load(f'imgs/pipe/{color}.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (self.image.get_width()*4, self.image.get_height()*4))
    self.speed_y = speed_y
    self.speed_x = speed_x
    self.counter = 0
    self.invert = invert
    if self.invert:
      self.image = pygame.transform.flip(self.image, False, True)
      self.rect = self.image.get_rect(center=(self.WIDTH + 50, 0 + y))
    else:
      self.rect = self.image.get_rect(center=(self.WIDTH + 50, self.HEIGHT - y))


  def stop(self):
    if not self.invert:
      if self.rect.top < self.HEIGHT/2:
        self.rect.top = self.HEIGHT
    else:
      if self.rect.bottom > self.HEIGHT/2:
        self.rect.bottom = self.HEIGHT/2

  def up_down(self):
    self.counter += 1
    if self.counter % 60 == 0:
        self.speed_y = -self.speed_y
    self.rect.y += self.speed_y

  def update(self):
    self.up_down()
    self.stop()
    self.rect.x -= self.speed_x
