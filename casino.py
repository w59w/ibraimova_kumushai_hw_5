from decouple import config
from logic import CasinoLogic

class CasinoGame:
    def __init__(self):
        self.starting_money = int(config('MY_MONEY'))
        self.current_money = self.starting_money
        self.logic = CasinoLogic()

    def start(self):
        print(f"Welcome to the Casino! You start with ${self.current_money}")
        while True:
            self.play_round()
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                break
        print(f"Game over! You ended with ${self.current_money}")

    def play_round(self):
        bet_amount = int(input("Place your bet: $"))
        if bet_amount > self.current_money:
            print("Sorry, you don't have enough money!")
            return
        slot_choice = int(input("Choose a slot (1-10): "))
        result = self.logic.play(slot_choice)
        if result:
            print(f"Congratulations! You won ${bet_amount * 2}")
            self.current_money += bet_amount
        else:
            print(f"Sorry, you lost ${bet_amount}")
            self.current_money -= bet_amount
        print(f"Your current balance: ${self.current_money}")
