#!usr/bin/python
#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

print("Let me tell you when in which year you'll turn a hundred years old! ^^")

age = int(input("Hey there, please enter your age: "))
counter = 1
while age < 0 or age > 100:
    print("I'm not fooled that easily...")
    age = int(input("Hey there, please enter your age: "))
    counter = counter + 1
    if counter >= 50000:
        age = 0
        break
else:
        print("Thanks for telling me your age")

name = raw_input("Now give your name please: ")
print("Great thanks.")

Current_year = int(2017)
Turn_hundred = Current_year - age + 100
print("Ok {} (age: {})".format(name, age)) 
print("Let me calculate when you will turn hundred")
print(Turn_hundred)

