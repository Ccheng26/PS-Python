# write a function that adds three numbers and divide
# the result by 3
w=9
result =0
# step 1: define the function, add arguments
def addingAndDividing(x, y, z):
    global result # to mutate global variable
    # step 2:
    print(f"w:{w}")
    print(f"")
    result = (x + y + z) / 3
    # step 3:
    print(f"result is {result}")
    return result
# step4
result1 = addingAndDividing(4, 5, 6)
result2 = addingAndDividing(7, 8, 9)
result3 = addingAndDividing(10, 110, 1110)

x = 9
print(f"result is {x}")
print(f"result for 1st call {result}")

##write a function that sums 3 numbers

total= 0
# def sum_three(x,y,z):
#     global total
#     total= x+y+z
#     print(f"{total}")

totalSet=[]
def sum_three_again(numList):
    total=0
    for int in numList:
        total+=int
    totalSet.append(total)

def lazy_print(arr):
    for int in arr:
        print(f"{int}")

# sum_three(19, -8, 9)
# sum_three(15, 9, 8)
# sum_three(30, -29, 5)
sum_three_again([19, -8, 9])
sum_three_again([15, 9, 8])
sum_three_again([30, -29, 5])
lazy_print(totalSet)

#Write a program that tells the user if their input is a positive number or negative number
def pos(num):
    if(type(num)!=int):
        print(f"sorry {num} is not a number")
    else:
        if(num>0):
            print(f"{num} is a positive number")
        else:
            print(f"{num} is a negative number")

#write a program that tells the user if their input is divisible by 4
def div_four(num):
    if(type(num)!=int):
        print(f"sorry {num} is not a number")
    else:
        if(num%4==0):
            print(f"{num} is divisible by four")
        else:
            print(f"{num} is not divisible by four")

#write a proram that tells if the input is in the range of 6 to 12 and 121 to 151
def in_range(num):
    if(type(num)!=int):
        print(f"sorry {num} is not a number")
    else:
        if(num<=12 and num>=6):
            print(f"{num} is between 6 and 12")
        elif(num<=151 and num>=121):
            print(f"{num} is between 121 and 151")
        else:
            print(f"not in the range of 6-12 or 121-151")

# write a function that takes 2 arguments
def check_a_thing(arg1, arg2):
    # if argument1 is greater than argument2,
    if(arg1>arg2):
        # divide the 1st arg by the 2nd arg
        res= arg1/arg2
        print(f"{arg1}/{arg2} is equal to {res}")
    # if argument2 is greater than argument1, 
    elif(arg2>arg1):
        #multiply argument1 by 10
        res= arg1*10
        print(f"{arg1} * 10 is equal to {res}")
    else:
        print("sorry not a valid input")
# call your function 3 times with different values

check_a_thing(5,1)
check_a_thing(1,5)
#an interesting thin happened here....
check_a_thing('a','b')
# evaled to a * 10 is equal to aaaaaaaaaa

#if arg1 is greater than arg2
# call the function to print a statement
# if arg2 is gerater than arg1 
# call the function to print a statement

def print_one():
    print("this is a call to function print_one")
def print_two():
    print("this is a call to function print_two")
def do_a_thing(arg1, arg2):
    if(arg1>arg2):
        print(f"{arg1}>{arg2}")
        print_one()
    elif(arg2>arg1):
        print(f"{arg1}<{arg2}")
        print_two()
    elif(arg1==arg2):
        print(f"{arg1}={arg2}")
    else:
        print("invalid input")
do_a_thing(1,5)