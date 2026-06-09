# File: bowling.py
# Description:  A Python program that calculates a bowler's average and handicap after three games
# Assignment Number: 4
#
#Name: Bismark Anakwa Kwadwo
# STUDENT ID: 2425403907
# Email: Mcriches061@gmail.com
# Grader: MR.AUGUSTUS BUCKMAN
# Slip days used this assignment: 0
#
# On my honor,Bismark Anakwa Kwadwo ,this programming assignment is my own work
# and I have not provided this code to any other student. .


def main():
    name = input("Enter your name: ")

    print()

    game1 = int(input("Enter Game 1: "))
    game2 = int(input("Enter Game 2: "))
    game3 = int(input("Enter Game 3: "))

    print()

    average = (game1 + game2 + game3) // 3
    handicap = ((200 - average) * 80) // 100

    print(f"{name}'s average is: {average}")
    print(f"{name}'s handicap is: {handicap}")


if __name__ == "__main__":
    main()