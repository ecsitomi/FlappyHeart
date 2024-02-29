#game.py
import pygame, random
from settings import *
from player import Player
from pipe import Pipe
from scenes import Scenes
from valentin import Valentin


class Game:

  def __init__(self, screen):
    self.WIDTH, self.HEIGHT = initialize()
    self.screen = screen
    self.pipes = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()
    self.valentin = pygame.sprite.GroupSingle()
    self.player.add(Player())
    self.counter = 0
    self.meters = 0
    self.frequency = 150
    self.bg_speed = 1
    self.create = True

  def create_pipe(self):
    if self.create:
      if len(self.pipes) < 7:
        self.counter += 1
        frequency = random.randint(120, 160)
        if self.counter % frequency == 0:
          color = random.randint(1, 5)
          y = random.randint(0, 100)
          speed_y = random.randint(0, 10)
          speed_x = random.randint(1, 5)
          invert = random.choice([True, False])
          self.pipes.add(Pipe(color, y, speed_y, speed_x, invert))

  def create_valentin(self):
    if self.create:
      if len(self.valentin) < 1:
        if self.counter % 24 == 0:
          random_height = random.randint(20, self.HEIGHT-20)
          random_speed =  random.randint(3, 7)
          self.valentin.add(Valentin(random_height, random_speed))

  def check_collision(self):
    player = self.player.sprite
    valentin = self.valentin.sprite
    for pipe in self.pipes:
      if pipe.rect.x < (-100):
        pipe.kill()
      if player.rect.colliderect(pipe.rect):
        self.handle_death()
    if player.rect.top < 0:
      player.rect.top = 0
    if player.rect.bottom > self.HEIGHT:
      self.handle_death()
    if self.valentin.sprite is not None:
      valentin = self.valentin.sprite
      if player.rect.colliderect(valentin.rect):
          lighting(self.screen, RED, 1000)
          self.valentin.empty()
          self.pipes.empty()
      if valentin.rect.x < (-100):
        valentin.kill()

  def handle_death(self):
    self.create = False
    self.bg_speed = 0
    player = self.player.sprite
    player.status = 'death'
    player.gravity_speed = 0
    player.fly_speed = 0
    player.heart_rate = 0
    for pipe in self.pipes:
      pipe.speed_x = 0
      pipe.speed_y = 0
    scenes = Scenes(self.screen)
    scenes.ending()
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          lighting(self.screen, RED, 1500)
          self.player.empty()
          self.pipes.empty()
          self.player.add(Player())
          self.counter = 0
          self.meters = 0
          self.bg_speed = 1

  def player_scores(self):
    player = self.player.sprite
    if player.status == 'beat' and self.counter % 20 == 0:
      self.meters += 1
    scenes = Scenes(self.screen)
    scenes.meters(self.meters)
    if player.heart_rate < 100:
      scenes.heart_rate(player.heart_rate, BLACK)
    elif 100 < player.heart_rate < 150:
      scenes.heart_rate(player.heart_rate, YELLOW)
    elif 150 < player.heart_rate < 200:
      scenes.heart_rate(player.heart_rate, RED)
    elif player.heart_rate > 200:
      self.handle_death()

  def run(self):
    infinite_bg(self.screen, self.bg_speed)
    self.pipes.update()
    self.player.update()
    self.valentin.update()
    self.pipes.draw(self.screen)
    self.valentin.draw(self.screen)
    self.player.draw(self.screen)
    self.check_collision()
    self.create_pipe()
    self.create_valentin()
    self.player_scores()
