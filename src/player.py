import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, level, start_x, start_y):
        super().__init__()
        self.level = level
        
        self.direction = DOWN
        self.load_sprite()
        
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        
        self.speed = PLAYER_SPEED
        self.dx = 0
        self.dy = 0
    
    def load_sprite(self):
        """Load single player sprite"""
        try:
            # Load the single player image
            self.image = pygame.image.load("assets/Player.png").convert_alpha()
            
            # Scale to appropriate size - wider to not be so slim
            self.image = pygame.transform.scale(self.image, (32, 32))
                
        except pygame.error as e:
            print(f"Could not load Player.png: {e}")
            print("Creating fallback sprite")
            self.create_fallback_sprite()
    
    def create_fallback_sprite(self):
        """Create a simple colored rectangle as fallback"""
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 100, 200))  # Blue character
    
    def handle_input(self, keys):
        """Handle WASD movement input"""
        self.dx = 0
        self.dy = 0
        
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.dy = -self.speed
            self.direction = UP
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.dy = self.speed
            self.direction = DOWN
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.dx = -self.speed
            self.direction = LEFT
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.dx = self.speed
            self.direction = RIGHT
    
    def update(self):
        """Update player position with collision detection"""
        old_x = self.rect.x
        old_y = self.rect.y
        
        self.rect.x += self.dx
        if self.check_collision() or self.check_bounds():
            self.rect.x = old_x
        
        self.rect.y += self.dy
        if self.check_collision() or self.check_bounds():
            self.rect.y = old_y 
    
    def check_bounds(self):
        """Check if player is going out of screen bounds"""
        return (self.rect.left < 0 or 
                self.rect.right > SCREEN_WIDTH or 
                self.rect.top < 0 or 
                self.rect.bottom > SCREEN_HEIGHT)
    
    def check_collision(self):
        """Check collision with level tiles"""
        corners = [
            (self.rect.left, self.rect.top),
            (self.rect.right - 1, self.rect.top),
            (self.rect.left, self.rect.bottom - 1),
            (self.rect.right - 1, self.rect.bottom - 1)
        ]
        
        for x, y in corners:
            tile_type = self.level.get_tile_at_pos(x, y)
            pass
        
        return False
    
    def draw(self, screen):
        """Draw the player"""
        screen.blit(self.image, self.rect) 