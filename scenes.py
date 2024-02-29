#scenes.py
from os import waitid_result
import pygame
from settings import RED, initialize, infinite_bg, setup_font, BLACK
from player import Player


class Scenes:

  def __init__(self, screen):
    self.screen = screen
    self.WIDTH, self.HEIGHT = initialize()
    self.player = pygame.sprite.GroupSingle()
    self.player.add(Player())
    self.bg_speed = 1

  def writing(self, text, size, x, y):
    font = setup_font(size)
    text = font.render(text, True, BLACK)
    text_rect = text.get_rect(center=(x, y))
    self.screen.blit(text, text_rect)
    pygame.display.update()

  def starting(self):
    infinite_bg(self.screen, self.bg_speed)
    self.writing('Flappy Heart', 56, self.WIDTH / 2, self.HEIGHT / 3)
    self.writing('Hit SPACE to fly', 18, self.WIDTH / 2, (self.HEIGHT /7)*6)
    player = self.player.sprite
    player.gravity_speed = 0
    self.player.update()
    self.player.draw(self.screen)

  def ending(self):
    self.writing('Game Over', 56, self.WIDTH / 2, self.HEIGHT / 2)
    self.writing('Hit SPACE to restart', 18, self.WIDTH / 2, (self.HEIGHT /7)*6)


