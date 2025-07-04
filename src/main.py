import pygame
import sys
from settings import *
from dungeon import Dungeon
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crawl & Brawl")
clock = pygame.time.Clock()

# Create dungeon instead of single level
dungeon = Dungeon()
player = Player(dungeon.get_current_room(), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

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
        
        # Store old position for room transitions
        old_x, old_y = player.rect.x, player.rect.y
        
        player.update()
        
        # Check for room transitions
        transition = dungeon.check_room_transition(player.rect.centerx, player.rect.centery)
        if transition:
            # Update player's level reference
            player.level = dungeon.get_current_room()
            
            # Move player to appropriate spawn position
            opposite_direction = {"right": "left", "left": "right", "top": "bottom", "bottom": "top"}
            spawn_x, spawn_y = dungeon.get_spawn_position(opposite_direction.get(transition, "center"))
            player.rect.x, player.rect.y = spawn_x, spawn_y

        # Draw everything
        screen.fill((0, 0, 0))
        dungeon.get_current_room().draw(screen)
        player.draw(screen)
        screen.blit(title_text, title_rect)
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
