#player.py
import pygame
from settings import import_folder, initialize

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.WIDTH, self.HEIGHT = initialize()
    self.animations = {'beat':[], 'death':[]}  
    self.import_character_assets()
    self.frame_index = 0  
    self.status = 'beat'
    self.animation_speed = 0.1
    self.rect = self.animations['beat'][self.frame_index].get_rect(center=(self.WIDTH/3, self.HEIGHT/2)) 
    self.gravity_speed = 10
    self.fly_speed = 18
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
    self.image = animation[int(self.frame_index)] 

  def fly(self):
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and self.status == 'beat':
      self.rect.y -= self.fly_speed
      self.heart_rate += 1
    else:
      self.heart_rate -= 1
      if self.heart_rate == 50:
        self.heart_rate = 50

  def gravity(self):
    self.rect.y += self.gravity_speed

  def update(self):
    self.animate()
    self.gravity()
    self.fly()
