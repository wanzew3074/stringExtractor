

systemInfo_file = open("test.txt", "r")

for systemInfo in systemInfo_file.readlines():
    print(systemInfo)

 
systemInfo_file.close()