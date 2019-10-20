# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program uses nested if statements


def main():
    # this function calculate if the year is a leap year
    # input
    year = input("Enter a year: ")
    print("")

    # process & output
    # try & except
    try:
        integerAsint = int(year)
        # checking if year entered is a leap year
        if (integerAsint % 4) == 0:
            if (integerAsint % 100) == 0:
                if (integerAsint % 400) == 0:
                    print("{} is a leap year!" .format(year))
                else:
                    print("{} is not a leap year." .format(year))
            else:
                print("{} is a leap year." .format(year))
        else:
            print("{} is not a leap year." .format(year))
    except Exception:
        print("This wasn't a valid entry. Please try again")
    finally:
        print("")
        print("Thank you for using my program!")


if __name__ == "__main__":
    main()
