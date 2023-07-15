# Import Libraries and Modules
import pygame as pg
import sys

def main():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit("Game Closed")

