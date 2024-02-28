import pygame, random
from settings import *
from player import Player
from pipe import Pipe

class Game:
  def __init__(self, screen):
    self.screen = screen
    self.pipes = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()
    self.player.add(Player())
    self.counter = 0
    self.meters = 0
    self.frequency = 150

  def create_pipe(self):
    self.counter += 1
    if counter % self.frequency == 0:
      color = random.choice(1,3)
      y = random.randint(-50, 50)
      speed = random.randint(0,10)
      self.pipes.add(Pipe(color, y, speed))
      

  def collision(self):
    player = self.player.sprite
    for pipe in self.pipes:
      if pipe.rect.x < (-100):
        pipe.kill()
      if player.rect.colliderect(pipe.rect):
        self.death()
    if player.rect.top > 0:
      player.rect.top = 0
    if player.rect.bottom > HEIGHT:
      self.death()  

  def death(self):
    player.status = 'death'
    player = self.player.sprite
    player.gravity = 0
    player.fly = 0
    player.heart_rate = 0
    for pipe in self.pipes:
      pipe.speed_x = 0    

  def run(self):
    self.pipes.draw(self.screen)
    self.pipes.run()
    self.player.draw(self.screen)
    self.player.run()
    self.create_pipe()
    self.collision()
    