import random

class Player:

    def __init__(self, num=None, score=0):
        self.num = num
        self.score = score


class Die:
    
    def __init__(self, side=None):
        self.side = side 
    
    def roll(self):
        self.side = random.randint(1, 6)
        return self.side


class Game:

    def __init__(self, player_count, player_one, player_two):
        self.max_score = 100
        self.scores = [player_one.score, player_two.score]
        self.player_count = player_count


if __name__ == '__main__':

    game_dice = Die()
    player_one = Player(num=1)
    player_two = Player(num=2)
    game = Game(2, player_one, player_two)


    while max(game.scores) < game.max_score:
        rolling = input(f'Player {player_one.num} rolling? Press "r" to roll. -->')

        if rolling:
            current_roll = game_dice.roll()
            print(f'Player {player_one.num} rolled a {current_roll}.')
            
