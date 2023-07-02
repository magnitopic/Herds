import random
import os
import time

class Jugador:
    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y
        self.score = 0

    def move(self):
        pass

class Food:
    def __init__(self, x, y, amount):
        self.x = x
        self.y = y
        slef.amount = amount


def create_players(num, DIM):
    players = []
    i = 0
    while (num):
        jugador_x = random.randint(0, DIM-1)
        jugador_y = random.randint(0, DIM-1)
        while self.tablero[jugador_x][jugador_y] != '·':
            jugador_x = random.randint(0, DIM-1)
            jugador_y = random.randint(0, DIM-1)
        players.append(Jugador(chr(65 + i), jugador_x, jugador_y))
        num -= 1

if __name__ == "__main__":
    size = 5
    player_num = 2
    food_num = 4
    players = create_players(player_num, size)
    for i in players:
        print(i.letter)