# define a function cheese_and_crackers that takes 2 args
# args are cheese_count and boxes of crackers
# print how many cheeses and crackers you have

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"cheese count: {cheese_count}")
    print(f"boxes o crackers: {boxes_of_crackers}")

# feed in nums directly
cheese_and_crackers(5, 10)

# assign variables globally and call function
cheese_count= 5
boxes_of_crackers=10
cheese_and_crackers(cheese_count, boxes_of_crackers)

#do math with function
cheese_and_crackers(4+3, 5-1)
#do math with variables in function arg
cheese_and_crackers(cheese_count+4, boxes_of_crackers+3)




































'''Actual book code

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have{boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese =10
amount_of_crackers= 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
'''