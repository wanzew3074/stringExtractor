from read import *
from write import *

def main():
    print("Please select operation -\n" \
          "1. Read\n" \
          "2. Write\n")

    select = int(input("Select operations form 1, 2:"))

    if select == 1:
        read()

    elif select == 2:
        write()

    else:
        print("Invalid input")


if __name__ == "__main__":
    main()