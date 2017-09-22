''' if statements
# create function to check number value
def grade(num):
	# format prompt input to number
	formatted_num=int(num)
	# run if statment to check grade
	if(formatted_num>=90 and formatted_num<=100):
		return 'A'
	elif(formatted_num>=80 and formatted_num<90):
		return 'B'
	elif(formatted_num>=70 and formatted_num<80):
		return 'C'
	elif(formatted_num>=55 and formatted_num<70):
		return 'D'
	elif(formatted_num>=0 and formatted_num<55):
		return 'F'
	else:
		return 'Invalid input'

# prompt user
num_given = input("Want to check your grade? Enter a number ")
# display grade statement
print("Your grade is " + grade(num_given))
'''

# make a for loop that prints from 5 to 15
'''
for x in range(5, 16):
	print ('inside the for loop')
	print(x)
	print(9+11)
	
	#print(x+1)
'''

'''for loops	
# write a for loop that prints the numbers from 5 to 15
for x in range(5,16):
	print(x)
# write a for loop that prints the numbers from 5 to 15 in increments of 3
for x in range(5,16,3):
	print(x)
# write a for loop that prints the numbers from 12 to 30 in multiples of 2
for x in range(2,30,2):
	print(x)
# print multiples of 3 from 3 to 90 in 
for x in range(2,90,3):
	print(x)
#a loop that prints out the letters of the word 'banana'
for x in 'banana':
	print(x)
'''

'''for loops
numbers =[]
for i in range(1,11):
	numbers.append(i)
print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers[1])
print(numbers[2])
for i in range(len(numbers)):
	print(numbers[i])
'''

#create a list that contains multiples of 2 from 12 to 48, including 48
mult_of_two=[]
for i in range(12,49,2):
		mult_of_two.append(i)
print(mult_of_two)