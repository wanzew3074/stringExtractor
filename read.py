import psutil
import platform


def read():
    extracted_txt = {}

    with open("readTest.txt", "r") as systemInfo:
        for line in systemInfo:
            content = line.split(" ")

            item = content[0]
            value = content[1]

            extracted_txt[item] = value

        print(extracted_txt)

    systemInfo.close()




