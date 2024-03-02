#game.py
import pygame, random
from settings import *
from player import Player
from pipe import Pipe
from valentin import Valentin


class Game:

  def __init__(self, screen):
    self.WIDTH, self.HEIGHT = initialize()
    self.right_side = self.WIDTH + 30
    self.screen = screen
    self.pipes = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()
    self.valentin = pygame.sprite.GroupSingle()
    self.scores = pygame.sprite.Group()
    self.player.add(Player(self.WIDTH, self.HEIGHT))
    self.counter = 0
    self.meters = 0
    self.bg_speed = 1
    self.create = True
    self.pipe_color = 1
    self.highest = 0

    self.sound = pygame.mixer.Sound(beat1)
    self.sound.play(-1)
    self.sound2 = pygame.mixer.Sound(beat2)
    self.sound2.stop()
    self.sound3 = pygame.mixer.Sound(beat3)
    self.sound3.stop()

    self.death_sound = pygame.mixer.Sound(death)
    self.death_sound.set_volume(0.3)
    self.death_sound.stop()

  def counting(self):
    if self.create:
      self.counter += 1
      if self.counter % 25 == 0:
        self.meters += 1
      elif self.counter % 143 == 0 and len(self.pipes) < 9:
        self.create_pipe()
      if self.counter % 1848 == 0 and len(self.valentin) < 1:
        self.create_valentin()

  def create_pipe(self):
    color = self.pipe_color
    y = random.randint(0, 100)
    speed_y = random.randint(0, 10)
    speed_x = random.randint(2, 7)
    invert = random.choice([True, False])
    self.pipes.add(
        Pipe(color, y, speed_y, speed_x, invert, self.right_side, self.HEIGHT))
    self.pipe_color += 1
    if self.pipe_color > 5:
      self.pipe_color = 1

  def create_valentin(self):
    random_height = random.randint(100, self.HEIGHT - 100)
    random_speed = 6
    self.valentin.add(Valentin(random_height, random_speed, self.right_side))

  def check_collision(self):
    player = self.player.sprite
    sound = pygame.mixer.Sound(kiss)
    for pipe in self.pipes:
      if pipe.rect.x < (-90):
        pipe.kill()
      elif player.rect.colliderect(pipe.rect):
        self.handle_death()
    if player.rect.top < 0:
      player.rect.top = 0
    elif player.rect.bottom > self.HEIGHT:
      self.handle_death()
    elif self.valentin.sprite is not None:
      valentin = self.valentin.sprite
      if player.rect.colliderect(valentin.rect):
        self.lighting(self.screen, WHITE, 150)
        player.heart_rate = 60
        self.valentin.empty()
        self.pipes.empty()
        sound.play()
      elif valentin.rect.x < (-90):
        valentin.kill()

  def handle_death(self):
    self.create = False
    self.bg_speed = 0
    player = self.player.sprite
    player.status = 'death'
    player.animation_speed = 0.1
    player.gravity_speed = 0
    player.fly_speed = 0
    player.heart_rate = 0
    for pipe in self.pipes:
      pipe.speed_x = 0
      pipe.speed_y = 0
    self.ending(file, self.highest, self.meters)
    self.restart()

  def lighting(self, display, color, msec):
    display.fill(color)
    pygame.time.delay(msec)
    self.writing('BOOM', 92, self.WIDTH / 2, self.HEIGHT / 2, font1, BLACK)
    pygame.display.flip()

  def writing(self, text, size, x, y, font, color):
    font = setup_font(size, font)
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=(x, y))
    self.screen.blit(text, text_rect)

  def starting(self):
    self.player.sprite.gravity_speed = 0
    infinite_bg(self.screen, self.bg_speed)
    self.writing('Flappy Heart', 96, self.WIDTH / 2, self.HEIGHT / 2, font1,
                 BLACK)
    self.writing('SPACE to fly', 56, self.WIDTH / 2, (self.HEIGHT / 9) * 8,
                 font1, BLACK)
    self.player.update()
    self.player.draw(self.screen)

  def ending(self, file, highest, score):
    self.sound.stop()
    if not pygame.mixer.Channel(0).get_busy():
      self.death_sound.play()
    self.writing('Game Over', 96, self.WIDTH / 2, self.HEIGHT / 3, font1, BLACK)
    self.writing('SPACE to restart', 56, self.WIDTH / 2, (self.HEIGHT / 9) * 8, font1, BLACK)
    try:
        with open(file, 'r+') as f:
            highest = int(f.read().strip())
            if highest > score:
                self.writing(f'Highest score: {highest} meters', 20, self.WIDTH / 2, self.HEIGHT / 2, font2, BLACK)
                self.writing(f'Your score: {score} meters', 20, self.WIDTH / 2, (self.HEIGHT / 2) + 30, font2, BLACK)
            else:
                self.writing(f'Your highest score: {score} meters', 20, self.WIDTH / 2, self.HEIGHT / 2, font2, BLACK)
                f.seek(0)
                f.write(str(score))
    except FileNotFoundError:
        with open(file, 'w') as f:
            f.write(str(score))
            self.writing(f'Your highest score: {score} meters', 20, self.WIDTH / 2, self.HEIGHT / 2, font2, BLACK)

  def restart(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        self.death_sound.stop()
        self.player.empty()
        self.valentin.empty()
        self.pipes.empty()
        self.counter = 0
        self.meters = 0
        self.bg_speed = 1
        self.player.add(Player(self.WIDTH, self.HEIGHT))
        self.create = True

  def player_bpm(self):
    color = BLACK
    player = self.player.sprite
    heart_rate = player.heart_rate
    if 0 < heart_rate <= 100:
      color = BLACK
      self.sound2.stop()
      self.sound3.stop()
      if not pygame.mixer.Channel(0).get_busy():
        self.sound.play(-1)
    elif 100 < heart_rate <= 150:
      color = YELLOW
      self.sound3.stop()
      self.sound.stop()
      if not pygame.mixer.Channel(0).get_busy():
        self.sound2.play(-1)
    elif 150 < heart_rate <= 200:
      color = RED
      self.sound2.stop()
      self.sound.stop()
      if not pygame.mixer.Channel(0).get_busy():
        self.sound3.play(-1)
    else:
      self.sound.stop()
      self.sound2.stop()
      self.sound3.stop()
      self.handle_death()
    self.writing(f'{round(heart_rate)} bpm', 24, self.WIDTH / 7,
                 self.HEIGHT / 8, font2, color)

  def player_meters(self, meters):
    self.symbols_surf_and_rect('imgs/hp.png',
                               (self.WIDTH / 12, self.HEIGHT / 8))
    self.symbols_surf_and_rect('imgs/flying_meters.png',
                               ((self.WIDTH / 10) * 8, (self.HEIGHT / 9) * 8))
    self.writing(f'{meters} meters', 24, (self.WIDTH / 9) * 8,
                 (self.HEIGHT / 9) * 8, font2, BLACK)

  def symbols_surf_and_rect(self, image_path, center):
    symbol_surf = pygame.image.load(image_path).convert_alpha()
    symbol_rect = symbol_surf.get_rect(center=center)
    self.screen.blit(symbol_surf, symbol_rect)

  def run(self):
    self.player.sprite.gravity_speed = 10
    infinite_bg(self.screen, self.bg_speed)
    self.pipes.update()
    self.player.update()
    self.valentin.update()
    self.pipes.draw(self.screen)
    self.valentin.draw(self.screen)
    self.player.draw(self.screen)
    self.check_collision()
    self.player_bpm()
    self.player_meters(self.meters)
    self.counting()
    
