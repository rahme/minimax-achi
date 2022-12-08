import pygame
from pixel_and_matrix import *
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ACHI AI')
screen.fill(BG_COLOR)

class board_gui:
    def __init__(self):
        self.draw_board_line()
        self.draw_board_circles()

    def draw_board_line(self):
        pygame.draw.line(screen, LINE_COLOR, (150,170), (150,280), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (150,320), (150,430), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (300,170), (300,280), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (300,320), (300,430), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (450,170), (450,280), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (450,320), (450,430), LINE_WIDTH)

        #horizontal
        pygame.draw.line(screen, LINE_COLOR, (170,150), (280,150), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (320,150), (430,150), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (170,300), (280,300), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (320,300), (430,300), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (170,450), (280,450), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (320,450), (430,450), LINE_WIDTH)
        
        #diagonal
        pygame.draw.line(screen, LINE_COLOR, (162,162), (287,287), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (313,313), (437,437), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (287,313), (163,437), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (313,287), (437,163), LINE_WIDTH)

    def draw_board_circles(self):
        pygame.draw.circle(screen, LINE_COLOR, (150,150), 20, 4)
        pygame.draw.circle(screen, LINE_COLOR, (150,300), 20, 4)
        pygame.draw.circle(screen, LINE_COLOR, (150,450), 20, 4)

        pygame.draw.circle(screen, LINE_COLOR, (300,150), 20, 4)
        pygame.draw.circle(screen, LINE_COLOR, (300,300), 20, 4)
        pygame.draw.circle(screen, LINE_COLOR, (300,450), 20, 4)

        pygame.draw.circle(screen, LINE_COLOR, (450,150), 20, 4)
        pygame.draw.circle(screen, LINE_COLOR, (450,300), 20, 4)
        pygame.draw.circle(screen, LINE_COLOR, (450,450), 20, 4)

    def draw_circle_token(self, row, col, player):
        x_coordinate, y_coordinate = matrix_to_pixel(row, col)
        if player == 1: pygame.draw.circle(screen, PLAYER_1_COLOR, (x_coordinate, y_coordinate), 20)
        elif player == 2: pygame.draw.circle(screen, PLAYER_2_COLOR, (x_coordinate, y_coordinate), 20)

    def erase_circle_token(self, row, col):
        x_coordinate, y_coordinate = matrix_to_pixel(row, col)
        pygame.draw.circle(screen, BG_COLOR, (x_coordinate, y_coordinate), 20)
        pygame.draw.circle(screen, LINE_COLOR, (x_coordinate, y_coordinate), 20, 4)

    def game_over(self, player, game_mode = ''):
        font = pygame.font.Font('freesansbold.ttf', 32)
        if player == 1:
            text = font.render("Game over: Player 1 wins!", True, TEXT_COLOR)
        else:
            if game_mode == 'pvp':
                text = font.render("Game over: Player 2 wins!", True, TEXT_COLOR)
            else:
                text = font.render("Game over: AI wins!", True, TEXT_COLOR)

        textPlacement = text.get_rect()
        textPlacement.center = (300, 80)

        screen.blit(text, textPlacement)