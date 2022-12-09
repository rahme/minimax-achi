import sys
import numpy
import pygame
from board_gui import *
from board_logic import *
from achi_ai import *

print("\nInitial Board:")
print(board_logic().circles,"\n")

def main():
    boardGui = board_gui()
    boardLogic = board_logic()
    achiAI = achi_ai()

    print("Welome! Lets play some Achi!")
    print("Would you like to play against a player (pvp) or AI (ai)? (pvp/ai)")
    boardLogic.gamemode = str(input())

    if(boardLogic.gamemode == 'ai'):
        print("What level do you want the AI to be? (0/1)")
        achiAI.level = int(input())

    print("Game will start. Please click on the GUI to place a token.\n")


    while True:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_coordinate = event.pos[0]
                y_coordinate = event.pos[1]
                selected_row, selected_col = pixels_to_matrix(x_coordinate, y_coordinate)

                # initially placing 4 tokens each (player)
                if boardLogic.placing == True and not (selected_row == -1 or selected_col == -1):
                    boardLogic.player_placing_token(selected_row, selected_col)
                    print(boardLogic.circles)
                    print('\n')
                # moving pieces (player)
                elif boardLogic.placing == False and not (selected_row == -1 or selected_col == -1):
                    boardLogic.player_moving_token(selected_row, selected_col)
                    print(boardLogic.circles)
                    print('\n')
                    
                    if boardLogic.gamemode == 'ai':
                        boardLogic.moving_clicks -= 1

            if boardLogic.gamemode == 'ai' and boardLogic.player == achiAI.player and boardLogic.running:
                pygame.display.update()
                if boardLogic.placing == True:
                    ai_row_choice, ai_col_choice = achiAI.ai_eval(boardLogic.placing, boardLogic.circles, boardLogic.player)
                    boardLogic.player_placing_token(ai_row_choice, ai_col_choice)
                    print(boardLogic.circles)
                    print('\n')
                elif boardLogic.placing == False and boardLogic.moving_clicks == 0:
                    temp_row, temp_col = boardLogic.get_blank_circles_placing(boardLogic.circles)[0]
                    ai_row_choice, ai_col_choice = achiAI.ai_eval(boardLogic.placing, boardLogic.circles, boardLogic.player)
                    boardLogic.player_moving_token(ai_row_choice, ai_col_choice)
                    boardLogic.player_moving_token(temp_row, temp_col)
                    print(boardLogic.circles)
                    print('\n')
                    boardLogic.moving_clicks_reset()

        if boardLogic.terminal_states(boardLogic.circles) == 1:
            boardGui.game_over(1)
        elif boardLogic.terminal_states(boardLogic.circles) == 2:
            boardGui.game_over(2, boardLogic.gamemode)

        pygame.display.update()

main()