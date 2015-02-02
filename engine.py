#!/usr/bin/env python3

from exceptions import *

class Game:
    def __init__(self, player_color="white", netinfo=None):
        """
        player_color may be "white" or "black".
        netinfo is the (ip, port) of the remote server, or None for local game.
        """
        self.player1_color  = player_color
        self.player2_color  = "white" if player_color == "black" else "black"

        self.board    = [[None] * 8] * 8   # board[column][line]
        self.turn     = "white"
        self.finished = False
        self.netinfo  = netinfo

        self.init_board()

    def init_board(self):
        """
        Initializes the board to the classical starting position
        """
        # TODO

    def play(self):
        """
        Plays a turn of the game, returns None.
        If the game is finished,  returns the color of the winner.
        """
        valid_move = False
        while not valid_move:
            move       = get_move()
            origin     = move[0]
            piece      = self.square(*origin)
            valid_move = piece.valid(move) and piece.color == self.turn

        piece.move((origin, destination))

        self.turn = "white" if self.turn == "black" else "black"

        if self.finished:
            if self.turn == self.player1_color:
                return self.player1_color
            else:
                return self.player2_color
        return None

    def get_move(self):
        """
        Returns a move = (origin, destination).
        This is only a debug implementation and may be overriden by the client.
        """
        column = input("column: ")
        line   = input("line: ")
        return (column, line)

    def square(column, line):
        """
        Returns the piece at given position.
        This function interfaces with position tuples nicer than
        the array access.
        """
        return self.board[column][line]
