#declare three variables with stored ints
num1= 15
num2=42
num3=6824824

# if the first input is > the second input run a condition
if num1>num2:
    print("num1 is greater than num2, lets get tacos")
elif num2<num1:
    print("num1 is less than num2, lets not get tacos")
else:
    print("pizza party")

# if num3 is > num2
if num3>num2:
    print("num3 is greater than num2, lets get pizza")
elif num3<num2:
    print("num3 is less than num2, no pizza for you")
else:
    print("icecream party")

if num1>num3:
    print("num1 is greater than num3, tacos confirmed")
else:
    print("num1 is not greater than num3, no taco for you")


''' Actual Exercise and study drill
people = 30
cars = 40
trucks = 15
#runs if statement checking if there are more cars than people, if true run body
if cars > people:
    print("We should take the cars.")
#if first condition eval to false, check this condition, if true run body
elif cars < people:
    print("We should not take the cars.") 
#if all other conditions eval to false, run this body
else: 
    print("We can't decide.")

#runs if statement checking if there are more trucks than cars, if true run body
if trucks > cars: 
    print("That's too many trucks.") 
#if prior condition false, check if trucks less than cars, if true run body
elif trucks < cars: 
    print("Maybe we could take the trucks.") 
#if all prior conditions eval to false, run this body
else: 
    print("We still can't decide.")
    # if evaled false for truck>cars and trucks<cars, run this check, if true run body
    if people > trucks: 
        print("Alright, let's just take the trucks.")
    # all other conditions eval to false, run body
    else:
        print("Fine, let's stay home then.")
'''