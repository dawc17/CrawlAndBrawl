import pygame
from settings import *

class Level:
    def __init__(self):
        self.tiles = {}
        self.load_grass_tileset()
        
        self.level_data = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,4,0,0,3,0,0,0,0,2,2,2,2,2,0,0,0,0,3,0,4,0,0,0,0],
            [0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0],
            [0,3,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,3,0,0,0],
            [0,0,0,0,4,0,2,2,2,2,2,2,2,2,2,2,2,0,4,0,0,0,0,0,0],
            [0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0],
            [0,4,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,4,0,0,0],
            [0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0],
            [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0],
            [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0],
            [0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0],
            [0,4,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,4,0,0,0],
            [0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0],
            [0,0,0,0,4,0,2,2,2,2,2,2,2,2,2,2,2,0,4,0,0,0,0,0,0],
            [0,3,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,3,0,0,0],
            [0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0],
            [0,4,0,0,3,0,0,0,0,2,2,2,2,2,0,0,0,0,3,0,4,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
    
    def load_grass_tileset(self):
        """Load the grass tileset and extract individual tiles"""
        try:
            tileset_path = "assets/TX Tileset Grass.png"
            tileset_image = pygame.image.load(tileset_path).convert_alpha()
            
            tileset_width = tileset_image.get_width()
            tileset_height = tileset_image.get_height()
            
            tiles_per_row = tileset_width // TILE_SIZE
            
            tile_index = 0
            for row in range(tileset_height // TILE_SIZE):
                for col in range(tiles_per_row):
                    x = col * TILE_SIZE
                    y = row * TILE_SIZE
                    tile_surface = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
                    tile_surface.blit(tileset_image, (0, 0), (x, y, TILE_SIZE, TILE_SIZE))
                    
                    # Store tiles we'll use
                    if tile_index < 10:
                        self.tiles[tile_index] = tile_surface
                    
                    tile_index += 1
                    
        except pygame.error as e:
            print(f"Could not load tileset: {e}")
            # Create fallback colored tiles
            self.create_fallback_tiles()
    
    def create_fallback_tiles(self):
        """Create colored rectangles as fallback if tileset loading fails"""
        colors = [
            (34, 139, 34),   # Forest green (grass)
            (160, 82, 45),   # Saddle brown (dirt)
            (128, 128, 128), # Gray (stone)
            (0, 100, 0),     # Dark green (dark grass)
            (50, 205, 50),   # Lime green (flower grass)
        ]
        
        for i, color in enumerate(colors):
            tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
            tile.fill(color)
            self.tiles[i] = tile
    
    def draw(self, screen):
        """Draw the entire level to the screen"""
        for row in range(len(self.level_data)):
            for col in range(len(self.level_data[row])):
                tile_type = self.level_data[row][col]
                x = col * TILE_SIZE
                y = row * TILE_SIZE
                
                if tile_type in self.tiles:
                    screen.blit(self.tiles[tile_type], (x, y))
    
    def get_tile_at_pos(self, x, y):
        """Get tile type at pixel position"""
        grid_x = x // TILE_SIZE
        grid_y = y // TILE_SIZE
        if 0 <= grid_y < len(self.level_data) and 0 <= grid_x < len(self.level_data[grid_y]):
            return self.level_data[grid_y][grid_x]
        return 0  # Default to grass if out of bounds 