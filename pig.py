import random


class Player:

    def __init__(self, num=None, total_score=0, temp_scores=[]):
        self.num = num
        self.total_score = total_score
        self.temp_scores = temp_scores


class Die:
    
    def __init__(self, side=None):
        self.side = side 
    
    def roll(self):
        self.side = random.randint(1, 6)
        return self.side


class Game:

    def __init__(self, player_count, player_one, player_two):
        self.max_score = 100
        self.scores = [player_one.total_score, player_two.total_score]
        self.player_count = player_count
        self.current_player = player_one

    def toggle_player(self, player_one, player_two):
        if self.current_player is player_one:
            self.current_player = player_two
            return self.current_player

        if self.current_player is player_two:
            self.current_player = player_one
            return self.current_player
    
    def start_game(self, player_one, player_two):
        while max(self.scores) < self.max_score:
            rolling = input(f"Player {self.current_player.num} rolling? Press 'r' to roll. -->")

            if rolling:
                current_roll = game_dice.roll()
                print(f'Player {self.current_player.num} rolled a {current_roll}.')

                if current_roll == 1:
                    print(f'That\'s too bad! Your score returns to 0.')
                    self.toggle_player(player_one, player_two)
                    print(self.current_player.num)


if __name__ == '__main__':

    game_dice = Die()
    player_one = Player(num=1)
    player_two = Player(num=2)
    game = Game(2, player_one, player_two)

    game.start_game(player_one, player_two)
