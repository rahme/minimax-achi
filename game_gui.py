import pygame as pg
from game_constants import *

def initialize_board():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Tutorial 1')
    screen.fill(BG_COLOR)
    pg.display.flip()
    