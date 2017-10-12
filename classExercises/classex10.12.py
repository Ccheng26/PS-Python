# create a list and fill values from 1-10 with a for loop

list_to_ten=[]
def to_ten():
    for i in range(1,11):
        list_to_ten.append(i)
    print(list_to_ten)

to_ten()

list_to_twenty=[]
def to_twenty():
    for i in range(1,20,2):
        list_to_twenty.append(i)
    print(list_to_twenty)

to_twenty()