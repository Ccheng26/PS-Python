from sys import argv
# read the WYSS section for how to run this

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

'''Study Drill
Error is ValueError: not enough values to unpack (expected 4, got 3)
The system will return an error since it is expecting the four parameters we've assigned them, it is trying to do something with each of those values and cannot if it's null

# script, p1, p2 = argv

# print("The script is called:", script)
# print("Your first parameter is:", p1)
# print("Your second parameter is:", p2)

#listis, para1, para2, para3, para4 = argv

#print(f"Your list of {listis} consists of {para1}, {para2}, {para3}, {para4}")

answer= input("Do you like making lists?")
print(f"that's okay, you'll learn")

script, parameter1, parameter2 = argv
print("The script is called:", script)
print("learn well and learn fast:", parameter1)
print("you could just ignore this:", parameter2)
'''