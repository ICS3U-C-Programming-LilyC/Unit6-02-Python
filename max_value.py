#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Dec/14/2023
# This program will generate 10 random numbers between 0 and 100
# and will determine the max number.
# My program uses a list and a loop to do what is listed above.

# Importing math and random modules.
import random
import constants


# Function that will determine the max number.
def find_min_value(list_of_ints):
    # Initializing the minimum value to be 100.
    minimum_value = 100

    # Using a For...in loop to find the minimum value.
    for random_number in list_of_ints:
        # Checking if the random number
        if random_number < minimum_value:
            # If the minimum value is less than the random number assign it as minimum_value variable.
            minimum_value = random_number

    # Return the final min value after the loop has checked all elements in the list.
    return minimum_value


def main():
    # Explaining my program to the user.
    print(
        "Welcome! My program will generate 10 random numbers between 0 and 100 and will determine the min\nnumber."
    )

    # Declaring variables to generate random numbers to an empty list.
    random_number = []
    # Declaring minimum value to be 0.
    minimum_value = 0

    # Using a For loop to display random numbers and determine the max value.
    for counter in range(0, constants.MAX_ARRAY_SIZE):
        # Generating random number between 0 and 100 and appending it to my random_number variable.
        random_number.append(random.randint(constants.MIN_NUMBER, constants.MAX_NUMBER))

        # Displaying the random numbers and what their position is in the list.
        print(
            "{} added to the list at position {}".format(
                random_number[counter], counter
            )
        )

    # Calling the function find_min_value() and assigning it to the variable min_value.
    min_value = find_min_value(random_number)

    # Displaying the max value to the user.
    print("\nThe minimum value is {}.".format(min_value))


if __name__ == "__main__":
    main()
