import sys, pygame
from gridcell import GridCell
from numpy.random import choice
from config import *
from utils import get_grid_coordinates
from dataclasses import dataclass

class Generation:
    number: int = 1
    grid_cells: dict = {}

    def __init__(self, grid_cells: list):
        for cell in grid_cells:
            x = cell.x_pos
            y = cell.y_pos
            self.grid_cells[(x, y)] = cell
        print(f'Initiated generation {self.number} with {len(grid_cells)} cells')

    def __repr__(self):
        return f'Generation #{self.number} with {len(self.grid_cells)} cells.'

@dataclass
class Game:
    keep_running: bool = True
    current_generation: Generation = None
    grid_coords: list = None

    def __post_init__(self):
        self.grid_coords = get_grid_coordinates()
        # could use strategy pattern to have different strategies and initialize the game with different patterns
        self.current_generation = self.initiate_random_generation()

    def initiate_random_generation(self) -> Generation:
        grid_cells = []
        for coord in self.grid_coords:
            x, y = coord
            draw = choice([True, False], p = [0.2, 0.8])
            grid_cell = GridCell(x_pos = x, y_pos = y, block_size = BLOCK_SIZE, alive = draw)
            grid_cells.append(grid_cell)
        new_gen = Generation(grid_cells = grid_cells)
        return new_gen

    def evolve(self):
         # Create new generation
        changed_cells = dict()

        for coords, cell in self.current_generation.grid_cells.items():
            neighbor_coords = cell.get_neighbors()
            alive_neighbor_cells = 0

            for coord in neighbor_coords:
                try:
                    if self.current_generation.grid_cells[coord].alive:
                        alive_neighbor_cells += 1
                except:
                    pass

            if cell.alive:
                if not (alive_neighbor_cells == 3  or alive_neighbor_cells == 2):
                    changed_cells[coords] = GridCell(x_pos = coords[0], y_pos = coords[1], block_size = BLOCK_SIZE, alive = False)
            else:
                if alive_neighbor_cells == 3:
                    changed_cells[coords] = GridCell(x_pos = coords[0], y_pos = coords[1], block_size = BLOCK_SIZE, alive = True)

        self.current_generation.grid_cells.update(changed_cells)   

    def run(self):
        clock = pygame.time.Clock()

        # empty cells list
        pygame.init()

        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        print(self.current_generation)
        while self.keep_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
            screen.fill(BLACK)


            for _, cell in self.current_generation.grid_cells.items():
                if cell.alive:
                    pygame.draw.rect(screen, WHITE, cell.rectangle, 1)

            pygame.display.flip()
            clock.tick(FPS)
            print(clock.get_fps())
            self.evolve()