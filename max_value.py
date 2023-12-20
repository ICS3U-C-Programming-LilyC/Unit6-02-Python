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
def find_max_value(arrayNumber):
    # Initializing counter to 0.
    counter = 0

    # Assigning the max equal to the array/list at position 0.
    max_value = arrayNumber[0]

    # Using a while loop to check all elements in the list and return the max number.
    while counter < constants.MAX_ARRAY_SIZE:
        # Check if the array/list at the position of counter is greater
        # than the max.
        if arrayNumber[counter] > max_value:
            # Assign new max number, which will be the arrayNumber at the
            # position counter.
            max_value = arrayNumber[counter]

        # Increment the counter.
        counter = counter + 1

    # Return the final max value after the loop has checked all elements in the list.
    return max_value


def main():
    # Explaining my program to the user.
    print(
        "Welcome! My program will generate 10 random numbers between 0 and 100 and will determine the max\nnumber."
    )

    # Declaring variables to generate random numbers to an empty list.
    random_number = []

    # Using a For loop to display random numbers and determine the max value.
    for counter in range(constants.MAX_ARRAY_SIZE):
        random_number.append(random.randint(constants.MIN_NUMBER, constants.MAX_NUMBER))

        # Displaying the random numbers and what their position is in the list.
        print(
            "{} added to the list at position {}".format(
                random_number[counter], counter
            )
        )

    # Calling the function find_max_value() and assigning it to the variable max_value.
    max_value = find_max_value(random_number)

    # Displaying the max value to the user.
    print("\nThe maximum value is {}.".format(max_value))


if __name__ == "__main__":
    main()
