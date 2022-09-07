import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter
        #we want all the player to get the next move given in a game

    def __init__(self, move):
        pass
class RandonComputerPlayer(Player):
    def __init__(self, letter):
        super(). __init__(letter)

    def get_move(self, game):
        square = random.choce(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = Falseval = None
        while not valid_square:
            square = input(self.letter +'\' turn. Input move(0-9):')
            #we're going to check that this is correct value by trying to cast
            #it to an integer, and if it's not , then we say its invalid
            #if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True   # if these are succesfull, then yay!
            except ValueError:
                print('Invalid square. Try again.')
        return val



#53:57