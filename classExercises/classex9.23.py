# 1.How many seconds are there in 42 minutes 42 seconds
# create a function to take in minutes and seconds
def min_to_sec(min, sec):
    # 1 min = 60 sec, convert the minutes and add remaining seconds, return val
    return min*60+sec

print(f"There are {min_to_sec(42,42)} seconds in 42 minutes and 42 seconds")

# 2.How many miles are there in 10 kilometers? Hint: There are 1.61 kilometers in a mile
# create a function to take in km
def km_to_mile(km):
    # 1.61 km = 1 mile, convert to miles and return val
    return km/1.61
print(f"There are {km_to_mile(10)} miles in 10 kilometers")

# 3. How much is 83 degress Fahrenheit in degree celsius
# create function to take in degree amount
def fahrenheit_to_celcius (degree):
    # formula for farenheit to celsius is listed below, return val
    return (degree- 32) * 5/9
print(f"83 degrees fahrenheit is {fahrenheit_to_celcius(83)} degrees in Celcius")

# 4. Import math library and find the square root of the numbers 81, 19, 16, 121
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
# 5. write a program that returns the area of a circle, r =9
# create a function 
def area_of_circle(radius):
    # formula is pi(r^2) return value
    return math.pow(radius,2) *math.pi
print(f"The area of a circle with a radius of 9 is {area_of_circle(9)}")

# 6. write a boolean function that returns true or false if the letter x is in a string provided by the user
# create a function that takes in a string
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
print(f"Does {x_prompt} have an x in it? {has_x(x_prompt)}")

# 7. write a boolean function that returns true or false if the letter a,e,i,o,u and in a string provided by the user
# create a function that takes in a string
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

# 6. What is the volume of a sphere with radius 5? The volume of a sphere with radius r is (4/3)πr3 
def vol_sphere(radius):
    # implement formula after importing math library(line 24), return value
    return (4/3)*math.pi*(math.pow(radius,3))
print(f"The volume of a sphere with a radius of 5 is {vol_sphere(5)}")

# 7. Write a boolean function that returns true if a given input is divisible by 3 or return false otherwise
def div_by_three(num):
    if(num%3==0):
        return True
    else:
        return False
in_num= input("Enter a number to check if it's divisible by 3 ")
print(f"Is {in_num} is divisible by 3? {div_by_three(int(in_num))}")

# 8. Import data/time library and print out today's data and current time
import time
import datetime
# print out time now
print(f"Current date and time is {datetime.datetime.now()}")

# 9. using the data time library, print out the current year
# strftime format, does a string format, putting the day of the year as a decimal number
print(f"Current year is {datetime.date.today().strftime('%j')}")

# 10. write a function that counts how  many times the letter a is repeated in a given word (get the work from the user as an input)
def repeat_a(string):
    counter=0
    string.lower()
    for l in string:
        if(l=='a'):
            counter+=1
    return counter
aWord = input("Enter in a word, see how many times a is repeated ")
print(f"The letter 'a' is repeated {repeat_a(aWord)} times.")

# write code that counts the number of letters in a word provided by the user
def word_count(sentence):
    word_store= sentence.split()
    # for ind in word_store:
    #     if(ind !="." or "?" or "!" or "," or "," or ""):
    #         word_store.split()
    return len(word_store)
sent = input("Enter a sentence, we'll see how many words are in here \n")
print(f"The sentence {sent} has {word_count(sent)} words in it")

'''Background Info:
If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to see if it is possible to form a triangle: 
If any of the three lengths is greater than the sum of the other two, 
then you cannot form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a "degenerate" triangle.) 
Write a function named triangle_check that takes three integers as arguments, and that prints either "Yes" or "No", depending on whether you can or cannot form a triangle from sticks with the given lengths. 
 Write a function that prompts the user to input three stick lengths, converts them to integers, and uses triangle_check to check whether sticks with the given lengths can form a triangle.
'''
# create a function that takes three arguments
def triangle_check(num1,num2,num3):
    # convert the sides to numbers
    side1=int(num1)
    side2=int(num2)
    side3=int(num3)
    
    # check the added sides
    if(side1 + side2 < side3):
        print("No")
        return
    elif(side2 + side3 < side1):
        print("No")
        return
    elif(side1 + side3 < side2):
        print("No")
        return
    else:
        # only print "Yes" if none of the above are true
        print("Yes")

num1=input("Enter the side and press enter ")
num2=input("Enter another side ")
num3=input("Enter the last side ")
triangle_check(num1,num2,num3)

# other version cause we were super ambitious!
def triangle_check_again():
    # get the string input
    num_string = input("Enter 3 numbers separated by a space ")
    # make an empty list
    nums=[]
    # split the string on spaces
    for num in num_string.split(' '):
        # add the numbers to the list
        nums.append(int(num))
    # check the addition values of the numbers against one side
    if nums[0]+nums[1]<nums[2]:
        print("No")
        return
    elif(nums[1] + nums[2] < nums[0]):
        print("No")
        return
    elif(nums[0] + nums[2] < nums[1]):
        print("No")
        return
    else:
        print("Yes")
triangle_check_again()