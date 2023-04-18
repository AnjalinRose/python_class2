
with open("numbers.txt",'r') as file:
    print(file.readlines())

with open("evens.txt",'a') as file:
    file.write("hello!")
