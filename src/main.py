import pygame
import sys
from settings import *
from level import Level
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crawl & Brawl")
clock = pygame.time.Clock()

level = Level()
player = Player(level, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

pixel_font = pygame.font.Font(None, 48)
title_text = pixel_font.render("Crawl & Brawl", True, (255, 255, 255))
title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 40))

def main():
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        
        player.update()

        screen.fill((0, 0, 0))
        level.draw(screen)
        player.draw(screen)
        screen.blit(title_text, title_rect)
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()