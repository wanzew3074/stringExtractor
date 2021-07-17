from read import *
from write import *
from setup import *


def main():
    print("Please select operation -\n" \
          "1. Read\n" \
          "2. Write\n" \
          "3. Setup\n")

    select = int(input("Select operations form 1,2,3: "))

    if select == 1:
        read()

    elif select == 2:
        write()

    elif select == 3:
        setup()

    else:
        print("Invalid input")


"""
if __name__ == "__main__":
    main()
"""
