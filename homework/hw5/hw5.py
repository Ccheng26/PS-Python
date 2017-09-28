# 1. Exercise 34: Accessing List Elements
#    See File ex34.txt

# 2. How many seconds are there in 42 minutes 42 seconds? 
def min_to_sec(min, sec):
    # 1 min = 60 sec, convert the minutes and add remaining seconds, return val
    return min*60+sec

print(f"There are {min_to_sec(42,42)} seconds in 42 minutes and 42 seconds")

# 3. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile 
def km_to_mile(km):
    # 1.61 km = 1 mile, convert to miles and return val
    return km/1.61
print(f"There are {km_to_mile(10)} miles in 10 kilometers")

# 4. How much is 83 degree Fahrenheit in degree celsius 
def fahrenheit_to_celcius (degree):
    # formula for farenheit to celsius is listed below, return val
    return (degree- 32) * 5/9
print(f"83 degrees fahrenheit is {fahrenheit_to_celcius(83)} degrees in Celcius")

# 5. import math library and find the square root of numbers 81, 19, 16, 121 
import math
# put items into array
num= [81,19,16,121]
# empty array to store sqroots
sqrts=[]
# create a function that takes in an array and stores sq roots of number list
def sqrt (arr):
    # iterate through array
    for x in arr:
        # add evaluated sq root to empty array
        sqrts.append(math.sqrt(x))
# run function on number list
sqrt(num)
# iterate over new num list and print
for x in sqrts:
    print(x)

# 6. write a program that returns the area of a circle, r = 9 
def area_of_circle(radius):
    # formula is pi(r^2) return value
    return math.pow(radius,2) *math.pi
print(f"The area of a circle with a radius of 9 is {area_of_circle(9)}")

# 7. write a boolean function that returns true or false if the letter x is in a string provided by the user 
def has_x(string_val):
    # convert string to upper case
    up= string_val.upper()
    # create a flag to store the boolean, false as a base condition
    flag=False
    # iterate through the string
    for x in up:
        # check if a character is x, if so return true, else, return false
        if(x=='X'):
            return True
    return flag
x_prompt=input("Enter a string, lets check if there's an x involved...")
print(f"Does '{x_prompt}' have an x in it? {has_x(x_prompt)}")

# 8. write a boolean function that returns true or false if any of the letter a, e, i, o, u and in a string provided by the user 
def has_vowels(str):
    # convert all characters to lower case
    lo =str.lower()
    # any - boolean that checks if there's anything in an iteratable is true
    # so first we're iterating through the string, and getting the individual characters
    # then we're checking if any character in the string has a vowel with char in the set defining the vowels
    # if there are vowels return true, since we are only checking for the presence of one char as a vowel
    if any(char in lo for char in ('a', 'e', 'i', 'o', 'u')):
        return True
    else:
        return False
# create a prompt that asks the user for a string
prompt= input("Put in a phrase, check if it's got vowels ")
print(f"The phrase '{prompt}', does it have vowels? {has_vowels(prompt)}")

# 9. What is the volume of a sphere with radius 5? The volume of a sphere with radius r is (4/3)πr3 
def vol_sphere(radius):
    # implement formula after importing math library(line 24), return value
    return (4/3)*math.pi*(math.pow(radius,3))
print(f"The volume of a sphere with a radius of 5 is {vol_sphere(5)}")

# 10. Write a boolean function that returns true if a given input is divisible by 3 or return false otherwise 
def div_by_three(num):
    if(num%3==0):
        return True
    else:
        return False
in_num= input("Enter a number to check if it's divisible by 3 ")
print(f"Is {in_num} is divisible by 3? {div_by_three(int(in_num))}")

# 11. Import data/time library and print out today’s data and current time 
import time
import datetime
# print out time now
current_time = datetime.datetime.now()
print(f"Current date and time is {current_time}")

# 12. Using the data time library, print out the current year 
print(f"Current year is {current_time.year}")

# 13. write a function that counts how many times the letter a is repeated in a given word (get the work from the user as an input) 
def repeat_a(string):
    counter=0
    string.lower()
    for l in string:
        if(l=='a'):
            counter+=1
    return counter
aWord = input("Enter in a word, see how many times a is repeated ")
print(f"The letter 'a' is repeated {repeat_a(aWord)} times.")

# 14. Write code that counts the number of letters in a word provided by the user 
def word_count(sentence):
    word_store= sentence.split()
    # for ind in word_store:
    #     if(ind !="." or "?" or "!" or "," or "," or ""):
    #         word_store.split()
    return len(word_store)
sent = input("Enter a sentence, we'll see how many words are in here \n")
print(f"The sentence '{sent}' has {word_count(sent)} words in it")

# 15. Wa function that counts down from 20 
def count_down(num):
    for i in range(num, 0, -1):
        print (i)
count_num=input("Give a number to count down from (ex 20) ")
count_down(int(count_num))
# Hard coded count_down(20)

# 16. write a function that tell if the given input in even or odd 
def isEven(inputNum):
    if inputNum.isnumeric():
        num = int(inputNum)
        if(num % 2 == 0):
            return "Even"
        elif (num % 2 == 1):
            return "Odd"
    else:
        print("Sorry not a valid input")
check_even= input("Give a number to check even or odd ")
print(f"The number {check_even} is {isEven(check_even)}")

# 17. find the length of the string given by the user as input using a counter variable (don’t use the built-in len function) 
def string_len(string):
    counter=0
    for i in string:
        counter+=1
    return counter
string_thing =input("Input a string to check its length ")
print(f"The string '{string_thing}' is {string_len(string_thing)} characters long")

# 18. write a loop that traverse through a string provided by the user and prints out one letter at a time
def word_traverse(sentence):
    word_list= sentence.split()
    for w in word_list:
        print(w)
sentences = input("Enter a sentence \n")
word_traverse(sentences)