#game.py
import pygame, random
from settings import *
from player import Player
from pipe import Pipe

class Game:
  def __init__(self, screen):
    self.WIDTH, self.HEIGHT = initialize()
    self.screen = screen
    self.pipes = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()
    self.player.add(Player())
    self.counter = 0
    self.meters = 0
    self.frequency = 150
    self.bg_speed = 1

  def create_pipe(self):
    if len(self.pipes ) < 7:
      self.counter += 1
      frequency = random.randint(120, 160)
      if self.counter % frequency == 0:
        color = random.randint(1,5)
        y = random.randint(0, 100)
        speed_y = random.randint(0,10)
        speed_x = random.randint(1,5)
        invert = random.choice([True, False])
        self.pipes.add(Pipe(color, y, speed_y, speed_x, invert))

  def check_collision(self):
    player = self.player.sprite
    for pipe in self.pipes:
      if pipe.rect.x < (-100):
        pipe.kill()
      if player.rect.colliderect(pipe.rect):
        self.handle_death()
    if player.rect.top < 0:
      player.rect.top = 0
    if player.rect.bottom > self.HEIGHT:
      self.handle_death()

  def handle_death(self):
    self.bg_speed = 0  
    player = self.player.sprite
    player.status = 'death'
    player.gravity_speed = 0
    player.fly_speed = 0
    player.heart_rate = 0
    for pipe in self.pipes:
      pipe.speed_x = 0  
      pipe.speed_y = 0    

  def run(self):
    infinite_bg(self.screen, self.bg_speed)
    self.pipes.update()
    self.player.update()
    self.pipes.draw(self.screen)
    self.player.draw(self.screen)
    self.check_collision()
    self.create_pipe()
    