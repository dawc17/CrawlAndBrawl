import pygame
from settings import *
import random

class Room:
    def __init__(self, room_id, room_type="basic"):
        self.room_id = room_id
        self.room_type = room_type
        self.tiles = {}
        self.load_dungeon_tiles()
        
        # Room connections (which directions have doors)
        self.doors = {
            DOOR_TOP: False,
            DOOR_BOTTOM: False,
            DOOR_LEFT: False,
            DOOR_RIGHT: False
        }
        
        # Generate room layout
        self.room_data = self.generate_room_layout()
    
    def load_dungeon_tiles(self):
        """Load dungeon tiles (walls and floors)"""
        try:
            # Load wall tileset
            wall_tileset = pygame.image.load("assets/TX Tileset Wall.png").convert_alpha()
            floor_tileset = pygame.image.load("assets/TX Tileset Stone Ground.png").convert_alpha()
            
            # Extract first tile from each tileset
            wall_tile = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
            wall_tile.blit(wall_tileset, (0, 0), (0, 0, TILE_SIZE, TILE_SIZE))
            
            floor_tile = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
            floor_tile.blit(floor_tileset, (0, 0), (0, 0, TILE_SIZE, TILE_SIZE))
            
            self.tiles[WALL] = wall_tile
            self.tiles[FLOOR] = floor_tile
            
        except pygame.error:
            # Fallback tiles
            self.create_fallback_tiles()
    
    def create_fallback_tiles(self):
        """Create simple colored tiles as fallback"""
        # Dark gray floor
        floor_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
        floor_tile.fill((64, 64, 64))
        self.tiles[FLOOR] = floor_tile
        
        # Light gray walls
        wall_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
        wall_tile.fill((128, 128, 128))
        self.tiles[WALL] = wall_tile
    
    def generate_room_layout(self):
        """Generate a basic room with walls around the edges"""
        layout = []
        
        for row in range(ROOM_HEIGHT):
            room_row = []
            for col in range(ROOM_WIDTH):
                # Walls around the edges, floor in the middle
                if (row == 0 or row == ROOM_HEIGHT - 1 or 
                    col == 0 or col == ROOM_WIDTH - 1):
                    room_row.append(WALL)
                else:
                    room_row.append(FLOOR)
            layout.append(room_row)
        
        return layout
    
    def add_door(self, direction):
        """Add a door in the specified direction"""
        self.doors[direction] = True
        
        # Modify room layout to include door
        if direction == DOOR_TOP:
            self.room_data[0][ROOM_WIDTH // 2] = FLOOR
        elif direction == DOOR_BOTTOM:
            self.room_data[ROOM_HEIGHT - 1][ROOM_WIDTH // 2] = FLOOR
        elif direction == DOOR_LEFT:
            self.room_data[ROOM_HEIGHT // 2][0] = FLOOR
        elif direction == DOOR_RIGHT:
            self.room_data[ROOM_HEIGHT // 2][ROOM_WIDTH - 1] = FLOOR
    
    def add_obstacles(self):
        """Add some random obstacles/pillars to make room interesting"""
        num_obstacles = random.randint(2, 5)
        
        for _ in range(num_obstacles):
            # Random position (not near edges or doors)
            x = random.randint(3, ROOM_WIDTH - 4)
            y = random.randint(3, ROOM_HEIGHT - 4)
            
            # Add a small wall obstacle
            self.room_data[y][x] = WALL
            if random.choice([True, False]):  # Sometimes add a 2x2 block
                self.room_data[y][x + 1] = WALL
                self.room_data[y + 1][x] = WALL
                self.room_data[y + 1][x + 1] = WALL
    
    def draw(self, screen):
        """Draw the room"""
        for row in range(len(self.room_data)):
            for col in range(len(self.room_data[row])):
                tile_type = self.room_data[row][col]
                x = col * TILE_SIZE
                y = row * TILE_SIZE
                
                if tile_type in self.tiles:
                    screen.blit(self.tiles[tile_type], (x, y))
    
    def get_tile_at_pos(self, x, y):
        """Get tile type at pixel position"""
        grid_x = x // TILE_SIZE
        grid_y = y // TILE_SIZE
        if 0 <= grid_y < len(self.room_data) and 0 <= grid_x < len(self.room_data[grid_y]):
            return self.room_data[grid_y][grid_x]
        return WALL  # Default to wall if out of bounds
    
    def is_walkable(self, x, y):
        """Check if position is walkable (not a wall)"""
        return self.get_tile_at_pos(x, y) != WALL
