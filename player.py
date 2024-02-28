import pygame
from settings import import_folder, initialize

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.WIDTH, self.HEIGHT = initialize()
    self.animations = {'beat':[],'death':[]}
    self.import_character_assets()
    self.frame_index = 0
    self.status = 'beat'
    self.animation_speed = 0.15
    self.image = self.animations['beat'][self.frame_index]
    self.rect = self.image.get_rect(center=(self.WIDTH/2,self.HEIGHT/2))
    self.gravity = 0.8
    self.fly = 16
    self.heart_rate = 65

  def import_character_assets(self): #animáció képeinek beolvasása
    character_path = 'imgs/player/'
    for animation in self.animations.keys(): 
        full_path = character_path + animation
        self.animations[animation] = import_folder(full_path,1.3)

  def animate(self):
    animation = self.animations[self.status]
    self.frame_index += self.animation_speed
    if self.frame_index >= len(animation):
        self.frame_index = 0

  def fly(self):
    keys=pygame.key.get_pressed()
    if keys == pygame.K_SPACE and self.status == 'beat':
      self.rect.y -= self.fly
      self.heart_rate += 10
    else:
      self.heart_rate -= 1
      if self.heart_rate == 50:
        self.heart_rate = 50

  def gravity(self):
    self.rect.y += self.gravity

  def run(self):
    self.animate()
    self.gravity()
    self.fly()
