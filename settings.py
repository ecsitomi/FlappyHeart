import pygame
from os import walk

WIDTH = None
HEIGHT = None
FPS = 60
BG_IMG = 'imgs/background.png'
bg_surf = None
bg_rect = None
player_size = 64

def initialize():
  pygame.init()
  monitor_info = pygame.display.Info()
  global WIDTH, HEIGHT
  WIDTH = monitor_info.current_w
  HEIGHT = monitor_info.current_h
  return WIDTH, HEIGHT

def background(image):
  pygame.init()
  global bg_surf, bg_rect, WIDTH, HEIGHT
  bg_surf = pygame.image.load(image).convert_alpha()
  original_width, original_height = bg_surf.get_size()
  new_height = HEIGHT
  new_width = int(original_width * (HEIGHT / original_height))
  bg_surf = pygame.transform.scale(bg_surf, (new_width, new_height))
  bg_rect = bg_surf.get_rect()
  return bg_surf, bg_rect

def import_folder(path,size): #képek beolvasása mappánként az animációhoz
  surface_list = []
  for _, _, img_files in walk(path):
      for image in img_files: 
          full_path = path+'/'+image
          image_surf = pygame.image.load(full_path).convert_alpha()
          new_width = player_size * size
          new_height = int(image_surf.get_height() * (new_width/image_surf.get_width()))
          small_image = pygame.transform.scale(image_surf, (new_width, new_height))
          surface_list.append(small_image)
  return surface_list
