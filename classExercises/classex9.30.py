'''
# 1.create a dictionary
# 2.add 3 key-value pairs to it
# 3.write a loop to iterate over the dictionary and print out each key, value pair
# 4.check if a given value is in the dictionary or not

dessert= dict()
dessert["pie"]= "pumpkin"
dessert["cake"]="chocolate"
dessert["tart"]="eggtart"
dessert["bun"]="custard"
    
for food in dessert:
    print(f"{food}: {dessert[food]}")
print(dessert)

def search_food(word):
    for food in dessert:
        if(word==dessert[food] or word==food):
            print(f"Yup {word} is in our dictionary")
            break
search_food("cake")
'''
# use dictionary as a counter: write a code to count how many times each character in a str appeared. use dictionaries to store the result
'''
# initial method
import string
# create a dictionary of the alphabet initialized to 0
string.ascii_lowercase or string.ascii_uppercase 
# make a function that takes in a string
def letter_count(str):
    # create a dictionary with letters going from a-z and A-Z, initialized to 0
    alpha = dict.fromkeys(string.ascii_letters, 0)
    # iterate over string
    for l in str:
        # check if letter is a key in dictionary if it is, add 1
        if (l in alpha):   
            alpha[l]+=1
    # check if counter has a greater value than 0, if so, print
    for c in alpha:
        if(alpha[c]>0):
            print(f"{c}:{alpha[c]}")
'''
# better way
'''
# declare function that takes in a string
def letter_count(string):
    # make a dictionary
    alpha = dict()
    # iterate through string
    for l in string:
        # if item in string is not in dictionary and is alphabetical initialize key value pair
        #  key is letter, value is 1 (first detected instance)
        if (l not in alpha and l.isalpha()):   
            alpha[l]=1
        # if item is already in dictionary, add 1
        elif (l.isalpha()):
            alpha[l] +=1
    # print dictionary
    print(alpha)
letter_count(input())
'''
# write a program that reads a text file and counts the number of lines

'''instructor example
def line_count():
    file_to_count= open("classex9.30.txt")
    count = 0
    for line in file_to_count:
        count+=1
    print(count)
    return count
line_count()
'''

''' using import
from sys import argv
script, filename= argv
word_count = 0
line_count = 0
lines = open(filename)

for line in lines:
    line_count+=1
    word_count+=len(line.split(" "))
lines.close()

# another way to do this, comment out ll 82-85
# lines.read() brings cursor to end of file
# content= lines.read()
# line_count= len(content.split("\n"))
# word_count= len(content.split(" "))

print(f"The file {filename} has {line_count} lines and {word_count} words")
'''

# for modules
# import wordcount as wc
# assigning aliases


