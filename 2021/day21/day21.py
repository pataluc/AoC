from itertools import permutations, product
from os import path
from sys import argv

deterministic_dice = 0
rolls = 0


def roll_deterministic_dice():
    global deterministic_dice, rolls
    deterministic_dice += 1
    rolls += 1
    if deterministic_dice > 100:
        deterministic_dice -= 100
    return deterministic_dice

class Player():
    def __init__(self, position):
        self.position = position
        self.score = 0

    def rolls(self, dice_value):
        self.position = ((self.position - 1 + dice_value) % 10 ) + 1
        self.score += self.position
        return self.has_won()

    def has_won(self):
        return self.score >= 1000

def get_3_rolls(dice_func):
    return (dice_func(), dice_func(), dice_func())
     
def game(starting, dice_func):
    p1, p2 = starting
    player1 = Player(p1)
    player2 = Player(p2)
    
    while True:
        player1.rolls(sum(get_3_rolls(dice_func)))
        if player1.has_won():
            return player2.score * rolls
        player2.rolls(sum(get_3_rolls(dice_func)))
        if player2.has_won():
            return player1.score * rolls

games = {}
def count_wins(position1, score1, position2, score2):
    global games
    if score1 >= 21:
        return (1,0)
    if score2 >= 21:
        return (0,1)
    if (position1, score1, position2, score2) in games:
        return games[(position1, score1, position2, score2)]
    
    result = (0,0)
    
    for dice1 in (1,2,3):
        for dice2 in (1,2,3):
            for dice3 in (1,2,3):
                sub_result1, sub_result2 = count_wins(position2, score2, (position1 + dice1 + dice2 + dice3) % 10, score1 + 1 + (position1 + dice1 + dice2 + dice3) % 10)
                result = (result[0] + sub_result2, result[1] + sub_result1)
    games[position1, score1, position2, score2] = result
    return result


assert game((4, 8), roll_deterministic_dice) == 739785
deterministic_dice = 0
rolls = 0
print("ex1 : %d" % game((9, 6), roll_deterministic_dice))


assert max(count_wins(4 - 1, 0, 8 - 1, 0)) == 444356092776315
print("ex1 : %d" % max(count_wins(9 - 1, 0, 6 - 1, 0)))