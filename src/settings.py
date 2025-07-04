SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576  # 18 tiles * 32 pixels = 576 (was 600)
FPS = 60

# Tile settings
TILE_SIZE = 32  # Each tile is 32x32 pixels
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE   # 25 tiles wide
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE # 18 tiles tall

# Tile types (indices in the tileset)
GRASS = 0
DIRT = 1  
STONE = 2
DARK_GRASS = 3
FLOWER_GRASS = 4

# Player settings
PLAYER_SPEED = 3
PLAYER_SIZE = 24

# Player directions (for sprite animation)
DOWN = 0  # Facing camera
UP = 1    # Facing away
LEFT = 2  # Facing left
RIGHT = 3 # Facing right (mirrored left)

# Dungeon tile types
FLOOR = 0
WALL = 1
DOOR = 2

# Dungeon settings
ROOM_WIDTH = GRID_WIDTH
ROOM_HEIGHT = GRID_HEIGHT
MAX_ROOMS = 10

# Door positions (for room connections)
DOOR_TOP = 0
DOOR_BOTTOM = 1
DOOR_LEFT = 2
DOOR_RIGHT = 3