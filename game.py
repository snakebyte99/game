import random

class Dice2:
    def roll(self):
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        return [first_dice, second_dice]

dice = Dice2()

print("""
***********************************
Welcome to Phi's Dice Game,
2 Dices, match the two numbers to win!
***********************************
[1,1] = 1 Credit
[2,2] = 2 Credits
[3,3] = 3 Credits
[4,4] = 4 Credits
[5,5] = 5 Credits
[6,6] = 6 Credits

""")

creds = ''
creds = int(input("How many credits do you want to buy? "))

while creds > 0:
    rollagain = input("Enter any key to continue... ")
    if rollagain != "":
        rolled_dice = (dice.roll())
        print("*******************************")
        print(rolled_dice)
        creds -= 1
        rollagain = ""
        x = rolled_dice[0]
        y = rolled_dice[1]
        if x == y:
            print("Winner Winner Winner")
            if x == 1:
                print("You have won 1 credits!")
                creds += 1
            elif x == 2:
                print("You have won 2 credits!")
                creds += 2
            elif x == 3:
                print("You have won 3 credits!")
                creds += 3
            elif x == 4:
                print("You have won 4 credits!")
                creds += 4
            elif x == 5:
                print("You have won 5 credits!")
                creds += 5
            elif x == 6:
                print("*****JACKPOT!!!!!!******")
                creds += 20
                print("You have won 20 credits!")
            print(f"You have {creds} credits left")
        else:
            print(f"You have {creds} credits left")

else:
    print("Game over, insert more money")


