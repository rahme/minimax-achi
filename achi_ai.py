from board_gui import *
from board_logic import *
import math
import random
import copy

class achi_ai:
    def __init__(self, level = 0, player = 2):
        self.level = level
        self.player = player

    def random_choice(self, placing, board, player):
        if placing == True:
            free_spots = board_logic().get_blank_circles_placing(board)
            rnd_choice = random.randrange(0, len(free_spots))

            return free_spots[rnd_choice]
        elif placing == False:
            surrounding_spots = board_logic().surronding_player_tokens_from_empty_spot(board, player)
            rnd_choice = random.randrange(0, len(surrounding_spots))

            return surrounding_spots[rnd_choice]        
                
    def minimax_placing(self, board, depth, isMaximizing):
        result = board_logic().terminal_states(board)
        if result != None:
            if result == 1: return -10
            if result == 2: return 10

        if(len(board_logic().get_blank_circles_placing(board)) == 0):
            return 0

        if(isMaximizing):
            bestScore = -math.inf

            for row in range(3):
                for col in range(3):
                    if board[row][col] == 0:
                        board[row][col] = 2
                        score = self.minimax_placing(board, depth + 1, False)
                        board[row][col] = 0
                        if (score > bestScore):
                            bestScore = score

            return bestScore
        else:
            bestScore = math.inf
            
            for row in range(3):
                for col in range(3):
                    if board[row][col] == 0:
                        board[row][col] = 1
                        score = self.minimax_placing(board, depth + 1, True)
                        board[row][col] = 0
                        if (score < bestScore):
                            bestScore = score

            return bestScore

    def best_move_placing(self, board, player):
        bestScore = -math.inf
        move = (0,0)
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = 2
                    score = self.minimax_placing(board, 0, False)
                    board[row][col] = 0
                    if (score > bestScore):
                        bestScore = score
                        bestMove = (row,col)

        return bestMove

    def minimax_moving(self, board, depth, isMaximizing):
        result = board_logic().terminal_states(board)
        if result != None:
            if result == 1: return -10
            if result == 2: return 10

        if(len(board_logic().get_blank_circles_placing(board)) == 1):
            return 0

        if(isMaximizing):
            bestScore = -math.inf

            surrounding_spots = board_logic().surronding_player_tokens_from_empty_spot(board, player)
            zero_row, zero_col = board_logic().get_blank_circles_placing(board)[0]
            moves = len(surrounding_spots)

            for place_to_move in range(0, moves):
                row, col = surrounding_spots[place_to_move]
                board[zero_row][zero_col] = 2
                board[row][col] = 0
                score = self.minimax_moving(board, 0, False)
                board[zero_row][zero_col] = 0
                board[row][col] = 2
                if (score > bestScore):
                    bestScore = score

            return bestScore
        else:
            bestScore = -math.inf

            surrounding_spots = board_logic().surronding_player_tokens_from_empty_spot(board, player)
            zero_row, zero_col = board_logic().get_blank_circles_placing(board)[0]
            moves = len(surrounding_spots)

            for place_to_move in range(0, moves):
                row, col = surrounding_spots[place_to_move]
                board[zero_row][zero_col] = 1
                board[row][col] = 0
                score = self.minimax_moving(board, 0, True)
                board[zero_row][zero_col] = 0
                board[row][col] = 2
                if (score < bestScore):
                    bestScore = score

            return bestScore

    def best_move_moving(self, board, player):
        bestScore = -math.inf
        move = (0,0)
        
        surrounding_spots = board_logic().surronding_player_tokens_from_empty_spot(board, player)
        zero_row, zero_col = board_logic().get_blank_circles_placing(board)[0]
        moves = len(surrounding_spots)

        for place_to_move in range(0, moves):
            row, col = surrounding_spots[place_to_move]
            board[zero_row][zero_col] = 2
            board[row][col] = 0
            score = self.minimax_moving(board, 0, False)
            board[zero_row][zero_col] = 0
            board[row][col] = 2
            if (score > bestScore):
                bestScore = score
                bestMove = (row, col)
            
        return bestMove


    def ai_eval(self, placing, main_board, player):
        if self.level == 0:
            # random choice
            move = self.random_choice(placing, main_board, player)
        else:
            if placing == True:
                move = self.best_move_placing(main_board, player)
            else:
                move = self.best_move_moving(main_board, player)

        return move