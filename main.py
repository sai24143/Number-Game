# Python code to play the 21 Number game

# returns the nearest multiple to 4
def nearest_multiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose():
    print("\n\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)

# checks whether the numbers are consecutive
def check_consecutive(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1] + 1:
            return False
    return True

# The main function for the game
def start():
    print("Welcome to the 21 Number Game!")
    print("Do you want to take the first chance? (Y/N)")
    chance = input('> ').strip().upper()

    xyz = []
    last = 0

    if chance == "Y":
        while last < 20:
            # Player's turn
            inp = int(input("\nHow many numbers do you want to enter? (1, 2, or 3): "))

            if 1 <= inp <= 3:
                comp = 4 - inp
            else:
                print("Wrong input. You are disqualified from the game.")
                lose()

            print("Now enter the values")
            for _ in range(inp):
                a = int(input('> '))
                xyz.append(a)

            # store the last element of xyz
            last = xyz[-1]

            # checks whether the input numbers are consecutive
            if check_consecutive(xyz):
                if last == 21:
                    lose()
                else:
                    # Computer's turn
                    for j in range(1, comp + 1):
                        xyz.append(last + j)
                    print("Order of inputs after computer's turn is: ")
                    print(xyz)
                    last = xyz[-1]
            else:
                print("\nYou did not input consecutive integers.")
                lose()

    elif chance == "N":
        comp = 1
        last = 0
        while last < 20:
            # Computer's turn
            for j in range(1, comp + 1):
                xyz.append(last + j)
            print("\nOrder of inputs after computer's turn is: ")
            print(xyz)
            last = xyz[-1]

            if last == 21:
                print("\nCONGRATULATIONS, YOU WIN!")
                exit(0)

            # Player's turn
            inp = int(input("\nHow many numbers do you want to enter? (1, 2, or 3): "))

            if 1 <= inp <= 3:
                comp = 4 - inp
            else:
                print("Wrong input. You are disqualified from the game.")
                lose()

            print("Now enter the values")
            for _ in range(inp):
                a = int(input('> '))
                xyz.append(a)

            # store the last element of xyz
            last = xyz[-1]

            # checks whether the input numbers are consecutive
            if check_consecutive(xyz):
                if last == 21:
                    lose()
            else:
                print("\nYou did not input consecutive integers.")
                lose()
    else:
        print("Wrong choice. Start again.")
        start()

# Start the game
start()
