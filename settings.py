#settings.py
import pygame
from os import walk

WIDTH = 1000
HEIGHT = 800
FPS = 60
BG_IMG = 'imgs/background.png'
BG_COLOR = (102, 204, 204)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (200, 75, 0)
bg_surf = None
bg_rect = None
background_x = 0
player_size = 64
#running = False
#starting = True
font1 = 'font/FlappyBirdy.ttf'
font2 = 'font/arial.ttf'
file = 'highscore.txt'
beat1 = 'sounds/beat111.wav'
beat2 = 'sounds/beat222.wav'
beat3 = 'sounds/beat333.wav'
death = 'sounds/death.wav'
kiss = 'sounds/kiss.wav'


def initialize():
  monitor_info = pygame.display.Info()
  global WIDTH, HEIGHT
  WIDTH = monitor_info.current_w
  HEIGHT = monitor_info.current_h
  return WIDTH, HEIGHT


def background(image):
  global bg_surf, bg_rect, WIDTH, HEIGHT
  bg_surf = pygame.image.load(image).convert_alpha()
  original_width, original_height = bg_surf.get_size()
  new_height = HEIGHT
  new_width = int(original_width * (HEIGHT / original_height))
  bg_surf = pygame.transform.scale(bg_surf, (new_width, new_height))
  bg_rect = bg_surf.get_rect()
  return bg_surf, bg_rect


def infinite_bg(screen, speed):
  bg_surf, bg_rect = background(BG_IMG)
  global background_x
  background_x -= speed
  if background_x <= -WIDTH:
    background_x = 0
  screen.blit(bg_surf,
              (background_x, screen.get_height() - bg_surf.get_height()))
  screen.blit(
      bg_surf,
      (background_x + WIDTH, screen.get_height() - bg_surf.get_height()))


def import_folder(path, size):  #képek beolvasása mappánként az animációhoz
  surface_list = []
  for _, _, img_files in walk(path):
    for image in img_files:
      full_path = path + '/' + image
      image_surf = pygame.image.load(full_path).convert_alpha()
      new_width = player_size * size
      new_height = int(image_surf.get_height() *
                       (new_width / image_surf.get_width()))
      small_image = pygame.transform.scale(image_surf, (new_width, new_height))
      surface_list.append(small_image)
  return surface_list


def setup_font(size, font):
  font_path = font
  font_size = size
  return pygame.font.Font(font_path, font_size)

