# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np

class Position:
    def __init__(self,board):
        self.numCol = 7
        self.numRow = 6
        self.position = np.zeros([self.numCol,self.numRow])
        self.mask = np.zeros([self.numCol,self.numRow])
        self.key = np.zeros([self.numCol,self.numRow])
        self.bottom = np.zeros([self.numCol,self.numRow])


    def canPlay(self,column):
        if self.board[column][0] == ' ':
            return True
        return False

    def play(self,column,My):
        if My:
            tile = 'O'
        else:
            tile = 'X'

        if self.canPlay(column):
            for y in range(self.numRow - 1, -1, -1):
                if self.board[column][y] == ' ':
                    self.board[column][y] = tile
                    self.nbMoves += 1
                    return
        print('Cannot play on this column')
        return

    def isWinningMove(self,column,myTurn):
        if myTurn:
            tile = 'O'
        else:
            tile = 'X'

        row = 0
        if not self.canPlay(column):
            return False

        for y in range(self.numRow - 1, -1, -1):
            if self.board[column][y] == ' ':
                row = y
                break

        # check horizontal spaces
        if column < 4:
            if self.board[column + 1][row] == tile and self.board[column + 2][row] == tile and self.board[column + 3][row] == tile:
                return True
        if column > 2:
            if self.board[column - 1][row] == tile and self.board[column - 2][row] == tile and self.board[column - 3][row] == tile:
                return True

        # check vertical spaces
        if row < 3:
            if self.board[column][row + 1] == tile and self.board[column][row + 2] == tile and self.board[column][row + 3] == tile:
                return True

        # check / diagonal spaces
        if column > 2 and row < 3:
            if self.board[column - 1][row + 1] == tile and self.board[column - 2][row + 2] == tile and self.board[column - 3][row + 3] == tile:
                return True

        # check \ diagonal spaces
        if column < 4 and row < 3:
            if self.board[column + 1][row + 1] == tile and self.board[column + 2][row + 2] == tile and self.board[column + 3][row + 3] == tile:
                return True

        return False

