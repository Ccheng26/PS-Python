#stores number into variable, formats string with int variable into variable x 
types_of_people = 10
x = f"There are {types_of_people} types of people."
#stores strings into variables, formats string with string variables into variable y
binary ="binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#prints stored formatted strings
print(x)
print(y)
#prints strings with variables with stroed strings in them
print(f"I said: {x}")
print(f"I also said: '{y}'")
#stores a boolean false into hilarious, stores a string that takes in an argument
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#prints string and adds boolean argument to it
print(joke_evaluation.format(hilarious))
#stores strings
w = "This is the left side of..."
e = "a string with a right side."
#prints both strings, concatinated differently
print(w + e)

'''
Study Drill
2. String is put into a string in line 7 in two places, and line 12 and 13
3. There are only 4 instances of storing a string in a string; others are type conversions, int to string (line 2-3), boolean to string (line 15-16), and string concatination (line 20-23)
4. Adding two strings combines both of them like a math operator, the + works by concatinating or combining both values, since it is not stored, it's not technically making a longers string by creating a new object, but printing both valuess