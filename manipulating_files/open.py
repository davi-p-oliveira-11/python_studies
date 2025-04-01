file = open("manipulating_files\lorem.txt", "r")

print(file.read())
print(file.readline())
print(file.readlines())

# tip
#while len(line := file.readline()):
#  print(line)

file.close()

