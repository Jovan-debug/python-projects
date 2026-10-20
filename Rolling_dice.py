import random
class Dice:
    valid_sides=[4,6,8,12,20]
    def __init__(self,side:int = 6):
        self.side=side if side  in self.valid_sides else 6
        

    def set_side(self,side_num:int):
        if side_num in self.valid_sides:
            self.side=side_num
            return True
        return False

    def roll(self,num_throws:int =1):
        return [random.randint(1,self.side) for x in range (num_throws)]


def valid_input(prompt:int):
    while True:
        raw_num=input(prompt).strip()
        if raw_num.isdigit() and  int(raw_num)>0:
            return int(raw_num)
        else:print("Enter a valid number of side")


def main():
    print("********Welcome to our Dice Rolling Game**********")
    dice=Dice()

    while True:
        choice=input("press p to play and q to exit:")

        if choice.strip().lower()=="p":
            num=int(input("Enter the number of side:"))
            dice.set_side(num)
            val_num=valid_input("Enter the number of rolls:")
            outcomes=dice.roll(val_num)
            print(f"outcomes:{outcomes}")
        elif choice.lower()=="q":
            print("Thank you for playing")
            break
        else : print("Enter a valid option please")

if __name__=="__main__":
    main()

    