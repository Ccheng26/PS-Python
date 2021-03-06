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


def find_prime(num):
    count = 0
    # one is not prime so we start from 2
    if(num < 2):
        print("Invalid input")
    else:
        for x in range(num, 2, -1):
            if (num % x == 0):
                count = count + 1
    if count == 2:
        print(f"{num} Is prime")
    else:
        print(f"{num} Is not prime")


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


def conversion(option, num):
    if(option == 1):
        return num * 1000
    elif(option == 2 or option == 4):
        return num * 1000000
    elif(option == 3):
        return num * 1000000000000
    else:
        return "Sorry invalid input"


def prompt():
    prime_in = input("Enter a number to check if its prime ")
    find_prime(int(prime_in))
    message = """Lets do a conversion: Select your conversion
	To convert from kilobytes to bytes, type 1 and hit enter
	To convert from mega byte to bytes, type 2 and hit enter
	To convert from terabyte to bytes, type 3 and hit enter
	To convert from terabyte to megabyte, type 4 and hit enter
	"""
    print(message)
    option = input()
    print("What number would you like to convert?", end=' ')
    num = input()
    con = conversion(int(option), int(num))
    print(f"You selected {option}, the result {con}")


prompt()

# deleted question 6
# Write a program that takes 5 arguments, checks if each argument is even or odd and returns the number of even or odd numbers / arguments
# declared function
def even_or_odd(num1, num2, num3, num4, num5):
	# store the function in an array
	num_set = [num1, num2, num3, num4, num5]
	# initialize counters and storage array
	even =0
	odd =0
	not_num=0
	casted= []
	# iterate through arguments supplied in array
	for vals in num_set:
		# check if argument is a number, if true, type cast to int, if false, store it in array without casting
		if vals.isnumeric():
			casted.append(int(vals))
		else:
			casted.append(vals)
	# iterate through casted list
	for vals in casted:
		# if value is integer do a check on if int is even or odd, then add to respective counters, if argument is not a number, add to invalid entry counter
		if type(vals) is int:
			if(vals%2 ==0):
				even+=1
			else:
				odd+=1
		else:
			not_num+=1
	print(f"There are {even} even numbers, {odd} odd numbers and {not_num} invalid entries")

# call function
def check_nums():
	print("Please give 5 numbers and press enter after each one, to check if they are even or odd")
	even_or_odd(input(), input(),input(), input(), input())

check_nums()