def read():
    systemInfo_file = open("readTest.txt", "r")

    for systemInfo in systemInfo_file.readlines():
        print(systemInfo)

    systemInfo_file.close()



def write():
    systemInfo_file = open("writeTest.txt", "a")

    systemInfo_file.write("\nTEST DATA2")

    systemInfo_file.close()




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
