import random

# Constants
RED = "\033[0;31m"
RESET = "\033[0m"

class Player:
    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y
        self.score = 0

    # players can only move one step at a time
    def move(self):
        pass

    def __str__(self):
        return f'\033[0;{str(ord(self.letter) - 34)}m{self.letter}\033[0m'


class Food:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(self.amount)


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['·']*size for _ in range(size)]
        self.players = []
        self.food = []

    def addPlayer(self, p):
        if (p.x <= self.size and p.y <= self.size):
            self.board[p.y][p.x] = p
            self.players.append(self.board[p.y][p.x])
        else:
            print(f"{RED}Error:\nPlayer position out of map{RESET}")

    def updatePlayer(self, p, x, y):
        if (x <= self.size and y <= self.size):
            self.board[p.y][p.x] = '·'
            self.board[y][x] = p
            p.x = x
            p.y = y
        else:
            print(f"{RED}Error:\nPlayer position out of map{RESET}")

    def addFood(self, food_num):
        for i in range(food_num):
            food_x = random.randint(0, self.size-1)
            food_y = random.randint(0, self.size-1)
            while board.board[food_x][food_y] != '·':
                food_x = random.randint(0, self.size - 1)
                food_y = random.randint(0, self.size - 1)
            self.board[food_y][food_x] = Food(random.randrange(1, 9))
            self.food.append(self.board[food_y][food_x])

    def printBoard(self):
        for row in self.board:
            print(*row)
        print()


def create_players(num, DIM, board):
    i = 0
    while (num):
        jugador_x = random.randint(0, DIM-1)
        jugador_y = random.randint(0, DIM-1)
        while board.board[jugador_x][jugador_y] != '·':
            jugador_x = random.randint(0, DIM-1)
            jugador_y = random.randint(0, DIM-1)
        board.addPlayer(Player(chr(65 + i), jugador_x, jugador_y))
        num -= 1
        i += 1


if __name__ == "__main__":
    size = 10
    player_num = 5
    food_num = 4
    board = Board(size)
    create_players(player_num, size, board)
    board.addFood(food_num)
    board.printBoard()

