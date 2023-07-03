import random
import os
import time
import sys

class Player:
    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y
        self.score = 0

    def move(self):
        pass

    def __str__(self):
        return self.letter

class Food:
    def __init__(self, x, y, amount):
        self.x = x
        self.y = y
        slef.amount = amount

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['·']*size for _ in range(size)]

    def addPlayer(self, p):
        if (p.x <= self.size and p.y <= self.size):
            self.board[p.y][p.x] = p
        else:
            print("Error:\nPlayer position out of map")

    def printBoard(self):
        for i, element1 in enumerate(self.board):
            print(*self.board[i])


def create_players(num, DIM, board):
    players = []
    i = 0
    while (num):
        jugador_x = random.randint(0, DIM-1)
        jugador_y = random.randint(0, DIM-1)
        while board.board[jugador_x][jugador_y] != '·':
            jugador_x = random.randint(0, DIM-1)
            jugador_y = random.randint(0, DIM-1)
        players.append(Player(chr(65 + i), jugador_x, jugador_y))
        board.addPlayer(players[i])
        num -= 1
        i += 1
    return players

if __name__ == "__main__":
    size = 5
    player_num = 2
    food_num = 4
    board = Board(size)
    players = create_players(player_num, size, board)
    board.printBoard()