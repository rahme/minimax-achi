# Import Libraries and Modules
import pygame as pg
import sys
from game_gui import *

# Define Main Function
def main():
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit("Game Closed")

# Run
initialize_board()
main()