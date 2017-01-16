NUMBER_OF_STICKS = 20
# When turn = 0, it's player 1's turn.
# When turn = 1, it's player 2's turn.
turn = 0

greetings = """
        Welcome to the Game of Sticks!

Each player takes turns picking up sticks.
You may pick up from 1 to 4
Sticks from a pile of 13 sticks.
The player who picks up the last stick wins.
"""
print(greetings)

while NUMBER_OF_STICKS > 0:
    print("There are {} stick(s) left.\n".format(NUMBER_OF_STICKS))
    print("Player {} - ".format(turn+1), end="")
    while True:
        sticks = int(input("How many sticks will you take? "))
        # When less than or equal to 4 sticks left,
        if NUMBER_OF_STICKS <= 4:
            # When the player picks the all remaining sticks,
            if sticks == NUMBER_OF_STICKS:
                print("Player {} wins!".format(turn+1))
                NUMBER_OF_STICKS -= sticks
                break
            elif 1 <= sticks < NUMBER_OF_STICKS:
                NUMBER_OF_STICKS -= sticks
                break
            else:
                print("You can't take {} sticks.".format(sticks))
                continue
        # When more than 4 sticks left, and player chooses btw 1 and 4 sticks.
        elif 1 <= sticks <= 4:
            NUMBER_OF_STICKS -= sticks
            break
        else:
            print("You can't take {} sticks.".format(sticks))
            continue
    # Change turns.
    turn = (turn+1)%2
