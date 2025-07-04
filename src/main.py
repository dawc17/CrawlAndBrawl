import pygame
import sys
from settings import *

# Initialize
pygame.init()

# Settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crawl & Brawl")
clock = pygame.time.Clock()

# Game loop
def main():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        # Draw
        screen.fill((0, 0, 0))  # black background
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()