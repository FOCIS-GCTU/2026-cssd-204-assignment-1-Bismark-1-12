# File: dice.py
# Description: Simulates multiple rounds of a simplified Craps game and outputs win statistics.
# Assignment Number: 6 
# 
# Name: Bismark Anakwa Kwadwo
# SID:  2425403907
# Email:mcriches061@gmail.com
# Grader: AUGUSTUS BUCKMAN
# 
# On my honor, Bismark Anakwa Kwadwo, this programming assignment is my own work
# and I have not provided this code to any other student.

import random

# Step 1: Initialize introductory print and random seed setup
print("This program simulates the dice game of craps.")
set_seed = input("Do you want to set the seed? Enter y for yes, anything else for no: ")

if set_seed == "y":
    seed_value = int(input("Enter an int for the initial seed: "))
    random.seed(seed_value)

# Step 2: Get the number of simulation rounds
rounds_to_run = int(input("Enter the number of rounds to run: "))

# Initialize tracking counters
total_wins = 0
max_rolls_in_any_round = 0

# Step 3: Core loop to run each individual round
for current_round in range(rounds_to_run):
    # Every round begins with an initial roll of two six-sided dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    initial_roll = die1 + die2
    rolls_in_this_round = 1
    
    # Check the immediate win or loss conditions for the initial roll
    if initial_roll == 7 or initial_roll == 11:
        total_wins += 1
    elif initial_roll == 2 or initial_roll == 3 or initial_roll == 12:
        pass  # Player loses immediately, no extra action needed
    else:
        # The initial roll establishes "the point"
        point = initial_roll
        keep_rolling = True
        
        # Sub-loop: Keep rolling until a matching point or a 7 is rolled
        while keep_rolling:
            sub_die1 = random.randint(1, 6)
            sub_die2 = random.randint(1, 6)
            sub_roll = sub_die1 + sub_die2
            rolls_in_this_round += 1
            
            if sub_roll == point:
                total_wins += 1
                keep_rolling = False
            elif sub_roll == 7:
                keep_rolling = False
                
    # Update the global maximum roll tracker if this round lasted longer
    if rolls_in_this_round > max_rolls_in_any_round:
        max_rolls_in_any_round = rolls_in_this_round

# Step 4: Format and print the final stats based on plural/singular requirements
if rounds_to_run > 0:
    # Determine "times" vs "time"
    if total_wins == 1:
        time_word = "time"
    else:
        time_word = "times"
        
    # Determine "rounds" vs "round"
    if rounds_to_run == 1:
        round_word = "round"
    else:
        round_word = "rounds"
        
    print("Player won " + str(total_wins) + " " + time_word + " in " + str(rounds_to_run) + " " + round_word + ".")
    print("Maximum number of rolls in a round = " + str(max_rolls_in_any_round))