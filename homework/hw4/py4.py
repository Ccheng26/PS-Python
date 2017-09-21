'''
1. See ex24.py
2. See ex25.py
3. See ex28.txt
4.
 a. https://stackoverflow.com/questions/156767/whats-the-difference-between-an-argument-and-a-parameter
 		Parameter is a variable in method definition, arguments are the data passed
 		Parameter: variable in declaration of function
 		Argument: value of actual that gets passed to function
 b. Python Docs: https://docs.python.org/2/library/string.html
 		See string_method.png
 		To Lowercase = "String".lower()
 		To Uppercase = "String".upper()

5. Write a Python unction that takes a user input as an integer and check the numer is prime or not.
 a. Hint: A prime number (or a prime is a natural number greater than 1) and that has no positive divisors other than 1 and itself.
'''
def find_prime (num):
	count =0
	#one is not prime so we start from 2
	if(num<2):
		print("Invalid input")
	else:
		for x in range(num, 2, -1):
			if (num% x ==0):
				count=count+1
	if count==1:
		print("Is prime")
	else:
		print("Is not prime")

find_prime(37)
find_prime(22)
'''
6. Write a program that does a conversion for the user. Your program should give user the following option to select from. Once the user selects the option and enters the input, your program should do the conversion accordingly.
 a. Convert from kilobytes to bytes = 1=> 1 000
 b. Convert from mega byte to bytes		1=> 1 000 000
 c. Convert from terabyte to bytes	=	1=> 1 000 000 000 000
 d. Convert from terabyte to megabyte	1=> 1 000 000
 	i. For Example:
 			Press 1 to convert from Kilobyte to byte
 			Press 2 to convert from megabyte to byte...
'''

message="""Lets do a conversion: Select your conversion
	To convert from kilobytes to bytes, type 1 and hit enter
	To convert from mega byte to bytes, type 2 and hit enter
	To convert from terabyte to bytes, type 3 and hit enter
	To convert from terabyte to megabyte, type 4 and hit enter
"""
def conversion(option, num):
	if(option == 1):
		num = num* 1000
		return num
	elif(option==2 or option==4):
		return num* 1000000
	elif(option==3):
		return num*1000000000000
	else:
		return "Sorry invalid input"
print(message)
option=input()
print("What number would you like to convert?", end=' ')
num = input()
print(num)
converted_num = conversion(option, num)
print(converted_num)
print(f"You selected {option}, the result is {converted_num}")
