import random
from room import Room
from settings import *

class Dungeon:
    def __init__(self):
        self.rooms = {}
        self.current_room_id = 0
        self.room_connections = {}
        self.generate_dungeon()
    
    def generate_dungeon(self):
        """Generate a simple linear dungeon"""
        # Create a series of connected rooms
        num_rooms = random.randint(5, MAX_ROOMS)
        
        for i in range(num_rooms):
            room = Room(i)
            
            # Add some obstacles to make rooms interesting
            if i > 0:  # Don't add obstacles to starting room
                room.add_obstacles()
            
            # Connect rooms linearly
            if i > 0:  # Not the first room
                room.add_door(DOOR_LEFT)  # Door to previous room
                self.rooms[i-1].add_door(DOOR_RIGHT)  # Previous room gets door to this room
            
            if i < num_rooms - 1:  # Not the last room
                room.add_door(DOOR_RIGHT)  # Door to next room
            
            self.rooms[i] = room
    
    def get_current_room(self):
        """Get the currently active room"""
        return self.rooms[self.current_room_id]
    
    def check_room_transition(self, player_x, player_y):
        """Check if player should transition to a new room"""
        current_room = self.get_current_room()
        
        # Check each door direction
        if current_room.doors[DOOR_RIGHT] and player_x >= SCREEN_WIDTH - 16:
            if self.current_room_id + 1 in self.rooms:
                self.current_room_id += 1
                return "right"
        
        elif current_room.doors[DOOR_LEFT] and player_x <= 16:
            if self.current_room_id - 1 in self.rooms:
                self.current_room_id -= 1
                return "left"
        
        elif current_room.doors[DOOR_TOP] and player_y <= 16:
            # Could connect to room above (if you add vertical connections)
            pass
        
        elif current_room.doors[DOOR_BOTTOM] and player_y >= SCREEN_HEIGHT - 16:
            # Could connect to room below (if you add vertical connections)
            pass
        
        return None
    
    def get_spawn_position(self, from_direction):
        """Get spawn position when entering room from a direction"""
        if from_direction == "right":
            return (SCREEN_WIDTH - 64, SCREEN_HEIGHT // 2)
        elif from_direction == "left":
            return (64, SCREEN_HEIGHT // 2)
        elif from_direction == "top":
            return (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 64)
        elif from_direction == "bottom":
            return (SCREEN_WIDTH // 2, 64)
        else:
            return (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Default center
