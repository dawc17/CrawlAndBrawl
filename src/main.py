import pygame
import sys
from settings import *
from level import Level

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crawl & Brawl")
clock = pygame.time.Clock()
level = Level()

pixel_font = pygame.font.Font(None, 48)
title_text = pixel_font.render("Crawl & Brawl", True, (255, 255, 255))
title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))

def main():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        
        level.draw(screen)
        
        screen.blit(title_text, title_rect)
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()