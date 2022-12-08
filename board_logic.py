import numpy
from board_gui import *

class board_logic:
    def __init__(self):
        self.circles = numpy.zeros((3,3))
        self.player = 1
        self.placing = True
        self.player_1_tokens = 4
        self.player_2_tokens = 4
        self.player_holding = False
        # attributes needed for AI
        self.moving_clicks = 2 # needed to allow for two clicks against AI in moving phase
        self.empty_circles = self.circles
        self.marked_circles = 0

        self.gamemode = 'pvp'
        self.running = True

    def place_player_number(self, row, col, player = 0):
        if player == 0: self.circles[row][col] = self.player
        else: self.circles[row][col] = player
        self.marked_circles += 1

        return self.circles

    def next_turn(self):
        self.player = self.player % 2 + 1

    def check_placing_over(self):
        if self.player_1_tokens == self.player_2_tokens == 0:
            self.placing = False
        return self.placing

    def check_if_available(self, row, col):
        return self.circles[row][col] == 0

    def subtract_token(self):
        if self.player == 1: self.player_1_tokens -= 1
        if self.player == 2: self.player_2_tokens -= 1

    def add_token(self):
        if self.player == 1: self.player_1_tokens += 1
        if self.player == 2: self.player_2_tokens += 1

    def player_placing_token(self, row, col,):
        if self.check_if_available(row, col):
            board_gui().draw_circle_token(row, col, self.player)
            self.place_player_number(row, col)
        self.subtract_token()
        self.next_turn()
        self.check_placing_over()

    def player_holding_change(self):
        if self.player_holding == False: self.player_holding = True
        else: self.player_holding = False

    def player_moving_token(self, row, col):
        # player picking up token
        if self.player_holding == False:
            if self.player == self.circles[row][col]:
                board_gui().erase_circle_token(row, col)
                self.marked_circles -= 1
                self.circles[row][col] = 0
                self.add_token()
                self.player_holding_change()
        
        # player placing down token
        elif self.player_holding == True:
            if self.circles[row][col] == 0:
                board_gui().draw_circle_token(row, col, self.player)
                self.place_player_number(row, col)
                self.subtract_token()
                self.player_holding_change()
                self.next_turn()

    # logic for win condition and ai below
    def terminal_states(self, board):
        # return 1 if player 1 wins
        # return 2 if player 2 wins
        winner = None

        # vertical win
        for col in range(COLS):
            if board[0][col] == board[1][col] == board[2][col] != 0:
                winner = board[0][col]

        # horizontal win
        for row in range(ROWS):
            if board[row][0] == board[row][1] == board[row][2] != 0:
                winner = board[row][0]

        # decending diagonal win
        if board[0][0] == board[1][1] == board[2][2] != 0:
            winner = board[1][1]

        # ascending diagonal win
        if board[2][0] == board[1][1] == board[0][2] != 0:
            winner = board[1][1]

        # check if tie (needed for AI)
        if winner == None and len(board_logic().get_blank_circles_placing(board)) == 0:
            return 0
        else: return winner

    def isfull(self):
        return self.marked_circles == 8

    def isempty(self):
        return self.marked_circles == 0

    def get_blank_circles_placing(self, board):
        blank_circles = []
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 0:
                    blank_circles.append((row, col))
                
        return blank_circles

    # function to help find surrounding free spots
    def surronding_player_tokens_from_empty_spot(self, board, player):
        # print("Player:",self.player)
        look_around = self.get_blank_circles_placing(board)[0]
        can_pick_up = []

        if (look_around == (0,0)):
            if board[0][1] == player: can_pick_up.append((0,1))
            if board[1][0] == player: can_pick_up.append((1,0))
            if board[1][1] == player: can_pick_up.append((1,1))
        if (look_around == (0,1)):
            if board[0][0] == player: can_pick_up.append((0,0))
            if board[0][2] == player: can_pick_up.append((0,2))
            if board[1][1] == player: can_pick_up.append((1,1))
        if (look_around == (0,2)):
            if board[0][1] == player: can_pick_up.append((0,1))
            if board[1][1] == player: can_pick_up.append((1,1))
            if board[1][2] == player: can_pick_up.append((1,2))

        if (look_around == (1,0)):
            if board[0][0] == player: can_pick_up.append((0,0))
            if board[1][1] == player: can_pick_up.append((1,1))
            if board[2][0] == player: can_pick_up.append((2,0))
        if (look_around == (1,1)):
            if board[0][0] == player: can_pick_up.append((0,0))
            if board[0][1] == player: can_pick_up.append((0,1))
            if board[0][2] == player: can_pick_up.append((0,2))
            if board[1][0] == player: can_pick_up.append((1,0))
            if board[1][2] == player: can_pick_up.append((1,2))
            if board[2][0] == player: can_pick_up.append((2,0))
            if board[2][1] == player: can_pick_up.append((2,1))
            if board[2][2] == player: can_pick_up.append((2,2))
        if (look_around == (1,2)):
            if board[0][2] == player: can_pick_up.append((0,2))
            if board[1][1] == player: can_pick_up.append((1,1))
            if board[2][2] == player: can_pick_up.append((2,2))

        if (look_around == (2,0)):
            if board[1][0] == player: can_pick_up.append((1,0))
            if board[1][1] == player: can_pick_up.append((1,1))
            if board[2][1] == player: can_pick_up.append((2,1))
        if (look_around == (2,1)):
            if board[2][0] == player: can_pick_up.append((2,0))
            if board[1][1] == player: can_pick_up.append((1,1))
            if board[2][2] == player: can_pick_up.append((2,2))
        if (look_around == (2,2)):
            if board[1][1] == player: can_pick_up.append((1,1))
            if board[1][2] == player: can_pick_up.append((1,2))
            if board[2][2] == player: can_pick_up.append((2,2))

        # print("Logic Empty:", look_around)
        # print("Logic pick up:", can_pick_up)

        return can_pick_up

    # allow for 2 human clicks during moving phase against AI
    def moving_clicks_reset(self):
        self.moving_clicks = 2