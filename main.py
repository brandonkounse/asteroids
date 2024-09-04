import pygame
from player import Player
from constants import *

def main():
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  running = True
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    player.update(dt)
    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
