import random

class NumberGuessingGame:
    def __init__ (self,min_val:int=1,max_val:int=100):
        self.min_val=min_val
        self.max_val=max_val
        self.attemps=0
        self.is_win=False
        self.reset_game()

    def reset_game(self):
        self.target_num=random.randint(self.min_val,self.max_val)
        self.attemps=0
        self.is_win=False

    def evaluate_guess(self,guess:int):
        self.attemps+=1

        if guess==self.target_num:
            return "🥳🥳🥳 You found it"

        elif guess<self.target_num:
            return "number too low"
        else:
            return "number too high"

def get_valid_guess(min_val:int,max_val:int):
        while True:
            raw_num = input(f"Enter a guess ({min_val}-{max_val}): ").strip()
            if raw_num.isdigit():
                num = int(raw_num)
                if min_val <= num <= max_val:
                    return num
                print(f"Out of bounds! Please enter a number between {min_val} and {max_val}.")
            else:
                print("Invalid entry! Please enter a valid positive whole number.")

def main():
    print("**** Welcome to the OOP Number Guessing Game ****")
    game = NumberGuessingGame(min_val=1, max_val=100)

    while True:
        guess=get_valid_guess(game.min_val,game.max_val)
        result=game.evaluate_guess(guess)

        if result=="🥳🥳🥳 You found it":
            print("🥳🥳🥳 You found it")
            break

        elif result=="number too low":
            print("number too low")

        else:print("number too high")


if __name__=="__main__":
    main()