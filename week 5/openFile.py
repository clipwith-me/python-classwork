# file = open('newFile.pdf', 'w')
# file.write("Hello world, This is amazing.")

# Reading a file

# file = open('newFile.pdf', 'r')
# data = file.read()
# print(data)

# Appending to a file
file = open('newFile.pdf', 'a')
file.write("By a Dewarming Machine")



# Error handling with try-except 
try:
    file = open('newFile.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("thanks for coding ")
    # file.close()