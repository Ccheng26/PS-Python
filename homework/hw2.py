# 3A

# declare function to take in array list and print out average
def aver(numList):
    #  variables to store numbers
    avg= 0.0
    total = 0
    # iterate through number set and get total
    for int in numList:
        total+= int
    # store the length of numer set
    given=len(numList)
    # artimetic to get average
    avg =total/given
    # print statment
    print(f"The average {given} given numbers of is {avg}")
# i.
aver([44, 64, 88, 53, 89])
# ii. 
aver([39, 45, 55, 90, 95, 96])
# iii. redefine array/numset
aver([54, -45, -10, 90])
# iv. redefine array/numset
aver([55, 65, 75, 95, 32])

'''
Alternatively you can hard code the numbers
i.
total= 44 + 64 + 88 + 53 + 89
given = 5
avg = total/given
print(f"The average {given} given numbers of is {avg}")
'''

# 3B
def isEven(inputNum):
    if(inputNum % 2 == 0):
        print(f"{inputNum}: is an even number")
    elif (inputNum % 2 == 1):
        print(f"{inputNum}: is an odd number")
    else:
        print("Sorry not a valid input")
# i. 4
isEven(4)
# ii 9
isEven(9)
# iii
isEven(19)
# iv
isEven(20)

'''
Alternatively you can hardcode the numbers
if(4%2==0):
    print("4: is an even number")
'''
