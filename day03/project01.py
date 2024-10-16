print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

ch1 = input("You are at  a crossroad, Where  do you want to go? Type 'left' of 'right'").lower()

if ch1 == 'left':
    ch2 = input("You have come to a lake . There  is an Island in the middle of the lake."
                "Type 'Wait' to wait for a boat. type 'swim' to swim across.").lower()
    if ch2 == 'wait':
        ch3 = input("You arrive at the Island unharmed."
                    "There is house with 3 doors. One red,"
                    "one yellow and one blue"
                    "which color do you choose?").lower()
        if ch3 == 'red':
            print("Its room full of fire. Game Over!")
        elif ch3 == 'yellow':
            print("You found the treasure. You Win!")
        elif ch3 == 'blue':
            print("You enter a room of beasts. Game Over!")
        else:
            print("You choose a door that does not exist. Game Over!")
    elif ch2 == 'swim':
        print("You got attacked by an angry trout. Game Over!")
    else:
        print("You choose wrong option. Game Over!")
elif ch1 == 'right':
    print("You fell in to a hole. Game Over!")
else:
    print("You choose wrong direction. Game Over!")
