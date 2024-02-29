#pipe.py
import pygame

class Pipe(pygame.sprite.Sprite):
  def __init__(self, color, y, speed_y, speed_x, invert, right_side, height):
    super().__init__()
    self.image = pygame.image.load(f'imgs/pipe/{color}.png').convert_alpha()
    self.HEIGHT = height
    self.speed_y = speed_y
    self.speed_x = speed_x
    self.counter = 0
    self.invert = invert
    if self.invert:
      self.image = pygame.transform.flip(self.image, False, True)
      self.rect = self.image.get_rect(center=(right_side, 0 + y))
    else:
      self.rect = self.image.get_rect(center=(right_side, height - y))

  def pipe_stop(self, height):
    if not self.invert:
      if self.rect.top < height/2:
        self.rect.top = height
    else:
      if self.rect.bottom > height/2:
        self.rect.bottom = height/2

  def pipe_up_down(self):
    self.counter += 1
    if self.counter % 60 == 0:
        self.speed_y = -self.speed_y
    self.rect.y += self.speed_y

  def update(self):
    self.pipe_up_down()
    self.pipe_stop(self.HEIGHT)
    self.rect.x -= self.speed_x
