#scenes.py
from os import waitid_result
import pygame
from settings import RED, initialize, infinite_bg, setup_font, BLACK, font1, font2
from player import Player


class Scenes:

  def __init__(self, screen):
    self.screen = screen
    self.WIDTH, self.HEIGHT = initialize()
    self.player = pygame.sprite.GroupSingle()
    self.player.add(Player())
    self.bg_speed = 1

  def writing(self, text, size, x, y, font,color):
    font = setup_font(size, font)
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=(x, y))
    self.screen.blit(text, text_rect)


  def starting(self):
    infinite_bg(self.screen, self.bg_speed)
    self.writing('Flappy Heart', 56, self.WIDTH / 2, self.HEIGHT / 3, font1,BLACK)
    self.writing('Hit SPACE to fly', 18, self.WIDTH / 2, (self.HEIGHT /7)*6, font1,BLACK)
    player = self.player.sprite
    player.gravity_speed = 0
    self.player.update()
    self.player.draw(self.screen)

  def ending(self):
    self.writing('Game Over', 56, self.WIDTH / 2, self.HEIGHT / 2, font1,BLACK)
    self.writing('Hit SPACE to restart', 18, self.WIDTH / 2, (self.HEIGHT /7)*6, font1,BLACK)

  def meters(self, meters):
    symbol_surf = pygame.image.load('imgs/flying_meters.png').convert_alpha()
    original_width, original_height = symbol_surf.get_size()  
    new_width = int(original_width * 0.15)
    new_height = int(original_height * 0.15)
    symbol_surf = pygame.transform.scale(symbol_surf, (new_width, new_height)) 
    symbol_rect = symbol_surf.get_rect(center=((self.WIDTH / 9) * 7, (self.HEIGHT / 8) * 7))
    self.screen.blit(symbol_surf, symbol_rect)
    self.writing(f'flew {meters} meters', 14, (self.WIDTH / 9) * 8, (self.HEIGHT / 8) * 7, font2,BLACK)

  def heart_rate(self, heart_rate,color):
    symbol_surf = pygame.image.load('imgs/hp.png').convert_alpha()
    original_width, original_height = symbol_surf.get_size() 
    new_width = int(original_width * 0.15)
    new_height = int(original_height * 0.15)
    symbol_surf = pygame.transform.scale(symbol_surf, (new_width, new_height)) 
    symbol_rect = symbol_surf.get_rect(center=(self.WIDTH / 12, self.HEIGHT / 8))
    self.screen.blit(symbol_surf, symbol_rect)
    self.writing(f'{heart_rate} bpm', 16, self.WIDTH / 7, self.HEIGHT / 8, font2,color)
