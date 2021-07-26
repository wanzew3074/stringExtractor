from read import *
from write import *
from setup import *

package = "psutil"


def main():
    print("Please select operation -\n" \
          "1. Read\n" \
          "2. Write\n" \
          "3. Setup\n")

    select = int(input("Select operations form 1,2,3: "))

    if select == 1:
        read_from_txt()

    elif select == 2:
        write()

    elif select == 3:
        install(package)

    else:
        print("Invalid input")


"""
if __name__ == "__main__":
    main()
"""
