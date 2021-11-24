from config import *

# I could have made this an object too
def get_grid_coordinates() -> list():
    coords = []
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            coords.append((x, y))
    return coords