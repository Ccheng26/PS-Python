ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")
# separates items by space and puts them in a list
stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# while list is less than 10 items, remove last item from more_stuff and append to next_one
while len(stuff) != 10:
    next_one = more_stuff.pop() 
    print("Adding: ", next_one) 
    stuff.append(next_one) 
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")
# print item at index 1
print(stuff[1])
print(stuff[-1]) # whoa! fancy, prints last item in array
print(stuff.pop()) # takes last item out
print(' '.join(stuff)) # what? cool! prints out the list separated by spaces
print('#'.join(stuff[3:5])) # super stellar! concats the 4th index item with #