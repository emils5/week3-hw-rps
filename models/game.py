from models.player import *
import random

class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def winner(self):
        if self.player_1.choice == self.player_2.choice:
            return None

        elif self.player_1.choice == "rock" and self.player_2.choice == "scissors":
            return self.player_1.name

        elif self.player_1.choice == "rock" and self.player_2.choice == "paper":
            return self.player_2.name

        elif self.player_1.choice == "paper" and self.player_2.choice == "rock":
            return self.player_1.name
        
        elif self.player_1.choice == "paper" and self.player_2.choice == "scissors":
            return self.player_2.name

        elif self.player_1.choice == "scissors" and self.player_2.choice == "paper":
            return self.player_1.name

        elif self.player_1.choice == "scissors" and self.player_2.choice == "rock":
            return self.player_2.name

    # def get_computer_move():
    #     options = ["rock", "paper", "scissors"]
    #     return options[random.randint(0,2)]
           


    


