#valentin.py
import pygame
from settings import initialize


class Valentin(pygame.sprite.Sprite):

  def __init__(self, random_height, random_speed, right_side):
    super().__init__()
    self.image = pygame.image.load('imgs/valentin.png').convert_alpha()
    self.rect = self.image.get_rect(center=(right_side, random_height))
    self.speed = random_speed
    self.speed_y = 2
    self.counter = 0

  def valentin_up_down(self):
    self.counter += 1
    if self.counter % 60 == 0:
        self.speed_y = -self.speed_y
    self.rect.y += self.speed_y
  
  def update(self):
    self.valentin_up_down()
    self.rect.x -= self.speed
