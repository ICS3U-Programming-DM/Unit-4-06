#!/usr/bin/env python3

# Created by Dylan Melo
# Created on Jan 2022
# Program displays RGB colours with a range from 0-50
# using multiple nested loops.

def main():
    print("welcome")
    red = 0
    green = 0
    blue = 0
    # Set range for loop

    for blue in range(1, 51, 1):
        print(" RGB: ( {}, {}, {}) ".format(blue, green, red))
        for green in range(1, 51, 1):
            print(" RGB: ( {}, {}, {}) ".format(blue, green, red))
            for red in range(1, 51, 1):
                print(" RGB: ( {}, {}, {}) ".format(blue, green, red))


if __name__ == "__main__":
    main()
