# syntax to read file
filepath = "file.txt"
# file = open(filepath,"r")
# print(file.read())
# file.close()



# or
with open(filepath,"r") as file:
    print(file.read())


# for i in  file:
#     print(i)