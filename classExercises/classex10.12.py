# create a list and fill values from 1-10 with a for loop

list_to_ten=[]
def to_ten():
    for i in range(1,11):
        list_to_ten.append(i)
    print(list_to_ten)
to_ten()

# other way to do this
# x=[]
# y=1
# for i in range(0,10):
#     list_to_ten[i]=y
#     y=y+1
# print(x)
list_to_twenty=[]
def to_twenty():
    for i in range(1,22,2):
        list_to_twenty.append(i)
    print(list_to_twenty)

to_twenty()