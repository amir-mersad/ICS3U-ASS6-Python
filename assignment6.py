#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: November 2019
# This program calculates the volume of a cylinder

import math


def main():
    # This function calculates the volume of a cylinder

    # Input
    semicuricular = input("Pleas enter the radius of the semicuricular: ")
    side = input("Please enter the length of the side"
                 "between the semicuriculars: ")
    try:
        semicuricular = float(semicuricular)
        side = float(side)
    except(Exception):
        print("Wrong input!!!")
        return
    # Process
    if semicuricular > 0 and side > 0:
        result = math.pi * (semicuricular ** 2) + 2 * semicuricular * side
    else:
        print("The number must be more then 0!")
        return

    # Output
    print("The area of the stadium is approximately {0:.2f}m^2".format(result))


if __name__ == "__main__":
    main()
