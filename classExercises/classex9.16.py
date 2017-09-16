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
# step4
addingAndDividing(4, 5, 6)
addingAndDividing(7, 8, 9)
addingAndDividing(10, 110, 1110)

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
