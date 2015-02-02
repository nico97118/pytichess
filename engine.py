#!/usr/bin/env python3

import piece
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

    def play(self):
        """
        Plays a turn of the game, returns None.
        If the game is finished,  returns the color of the winner.
        """
        valid_move = False
        while not valid_move:
            move       = get_move()
            origin     = move[0]
            piece      = self.at(*origin)
            valid_move = piece.valid(move) and piece.color == self.turn

        piece.move((origin, destination))

        self.turn = "white" if self.turn == "black" else "black"

        if self.finished:
            if self.turn == self.player1_color:
                return self.player1_color
            else:
                return self.player2_color
        return None

    def init_board():
        """
        Initializes the board with the classical chess starting position
        """
        self.board[0][0] = piece.Rook("white")
        self.board[1][0] = piece.Knight("white")
        self.board[2][0] = piece.Bishop("white")
        self.board[3][0] = piece.Queen("white")
        self.board[4][0] = piece.King("white")
        self.board[5][0] = piece.Bishop("white")
        self.board[6][0] = piece.Knight("white")
        self.board[7][0] = piece.Rook("white")

        self.board[0][7] = piece.Rook("black")
        self.board[1][7] = piece.Knight("black")
        self.board[2][7] = piece.Bishop("black")
        self.board[3][7] = piece.Queen("black")
        self.board[4][7] = piece.King("black")
        self.board[5][7] = piece.Bishop("black")
        self.board[6][7] = piece.Knight("black")
        self.board[7][7] = piece.Rook("black")

        for i in range(8):
            self.board[i][1] = piece.Pawn("white")
            self.board[i][1] = piece.Pawn("black")


    def get_move(self):
        """
        Returns a move = (origin, destination).
        This is only a debug implementation and may be overriden by the client.
        """
        o_column = input("column: ")
        o_line   = input("line: ")
        d_column = input("column: ")
        d_line   = input("line: ")
        return ((o_column-1, o_line-1),
                (d_column-1, d_line-1))

    def at(column, line):
        """
        Returns the piece at given position.
        This function interfaces with position tuples nicer than
        the array access.
        """
        return self.board[column][line]

    def move(origin, destination):
        """
        Moves a piece from origin to destination
        Raises a InvalidMoveException if no piece is present at the given
        location
        """
        opiece = at(*origin)

        if (not opiece.is_move_valid(origin, destination)
            or  opiece.is_ally(destination)):
            raise InvalidMoveException

        at(*destination) = at(*origin)
        at(*origin)      = None
