from sys import argv
#takes in two arguments
script, filename= argv
#open a text file
txt= open(filename)
#prints file name
print(f"Here's your file {filename}:")
#prints text in file
print(txt.read())
#close file
txt.close()

#prompt user
print("Type that filename again:")
#store file input
file_again = input("> ")
#opens file name stored in file_again
txt_again=open(file_again)
#prints text in file
print(txt_again.read())
#close file
txt_again.close()

'''Study Drill
Removing lines 10-15

from sys import argv

script, filename= argv

txt= open(filename)

print(f"Here's your file {filename}:")

print(txt.read())
txt.close()

Using input and prompting the user allows you to be more specific as opposed to running a program if you do not know the number of parameters or file names

'''