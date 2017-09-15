#imports argv form module sys
from sys import argv
#create variables to store arguments
script, filename= argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
#write to file
print("Opening the file...")
#open file with write permission
target = open(filename, 'w')
#changes the size of the file, reduces size of file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write to these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target.close()

'''Study Drill

'''