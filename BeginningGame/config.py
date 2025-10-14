# config.py

# Grid and Room Settings
GRID_ROWS = 5
GRID_COLS = 5
ROOM_WIDTH = 150
ROOM_HEIGHT = 150
WALL_THICK = 4
DOOR_SIZE = 30

# Player Settings
PLAYER_RADIUS = 10
PLAYER_SPEED = 100

# Screen Size
WIDTH = ROOM_WIDTH * GRID_COLS
HEIGHT = ROOM_HEIGHT * GRID_ROWS

# Colors (R, G, B)
BG_COLOR = (20, 20, 24)
WALL_COLOR = (200, 200, 200)
PLAYER_COLOR = (100, 200, 255)
BOX_COLOR = (205,163,100)

# Frames Per Second
FPS = 60

# --- Player appearance ---
PLAYER_IMAGE_PATH = "./goose.png"  # transparent PNG, e.g. 48x48
PLAYER_IMAGE_SIZE = (48, 48)             # w, h in pixels
PLAYER_RADIUS = 24                       # half of width; used by your collision