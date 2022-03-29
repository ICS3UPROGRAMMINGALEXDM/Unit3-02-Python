#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description:

import math
import random
import sys

def main():
    while True:
        r_num = random.randint(1,15)
        print("I just generated a random number between 1-15. Can you Guess it correctly?")
        print(r_num)

        while True:
            u_num = int(input("Input your number below:\n"))

            if u_num == r_num:
                print("Congratulations, you guessed the number correctly!!")
                answer = input("Would you like to play again? (y/n):").strip().lower()

                if answer == "y":
                    print("Okay")
                    break
                else:
                    print("Okay")
                    sys.exit()
                    
                
            else:
                print("Uh oh, wrong answer. Guess again!")


if __name__ == "__main__":
    main()