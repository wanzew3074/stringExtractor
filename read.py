def read():
    systemInfo_file = open("readTest.txt", "r")

    for systemInfo in systemInfo_file.readlines():
        print(systemInfo)

    systemInfo_file.close()










