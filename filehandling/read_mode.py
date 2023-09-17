# This is the read mode.
# "r"
# 1

# var_name = open("file1.txt",  "r")
# for x in var_name:
#     print(x)
    
# 2
# file_read=open("file1.txt",'r')
# print(file_read.read())
    
# 3
# with open("file1.txt") as file_read:
#     text = file_read.read()
# print(text)



with open('file1.txt') as file_open:
    for line in file_open:
        data=line.split()
        print(data)