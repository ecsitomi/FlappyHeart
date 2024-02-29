#valentin.py
import pygame, math
from settings import initialize


class Valentin(pygame.sprite.Sprite):

  def __init__(self, random_height, random_speed):
    super().__init__()
    self.WIDTH, self.HEIGHT = initialize()
    self.image = pygame.image.load('imgs/valentin.png').convert_alpha()
    self.rect = self.image.get_rect(center=(self.WIDTH + 50, random_height))
    self.speed = random_speed
    self.amplitudo = 50
    self.frequency = 0.01
    self.time_passed = 0
  
  def update(self):
    self.rect.x -= self.speed
    self.time_passed += 1
    self.rect.y = int(self.rect.y + self.amplitudo * math.sin(self.time_passed * self.frequency))  # hullám szerű mozgás
