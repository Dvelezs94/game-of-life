from dataclasses import dataclass
from pygame import Rect
from config import *

@dataclass
class GridCell:
    x_pos: int
    y_pos: int
    alive: bool
    block_size: int
    rectangle: Rect = None

    def __post_init__(self):
        self.rectangle = Rect(self.x_pos, self.y_pos, self.block_size, self.block_size)

    def get_neighbors(self) -> list:
        x = self.x_pos
        y = self.y_pos
        neighbors = [None] * 8
        # graphical explanation of the grid position
        # [
        #     (20, 30),(20, 40),(20, 50),
        #     (30, 30),(30, 40),(30, 50),
        #     (40, 30),(40, 40),(40, 50)

        #     0,0,0,0,1,0,0,0,0
        # ]
        neighbors[0] = (x - BLOCK_SIZE, y - BLOCK_SIZE)
        neighbors[1] = (x - BLOCK_SIZE, y)
        neighbors[2] = (x - BLOCK_SIZE, y + BLOCK_SIZE)
        neighbors[3] = (x, y - BLOCK_SIZE)
        neighbors[4] = (x, y + BLOCK_SIZE)
        neighbors[5] = (x + BLOCK_SIZE, y - BLOCK_SIZE)
        neighbors[6] = (x + BLOCK_SIZE, y)
        neighbors[7] = (x + BLOCK_SIZE, y + BLOCK_SIZE)
        return neighbors