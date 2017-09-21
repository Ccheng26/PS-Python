# declare a multiline text thing and call it poem
poem = """ Hi everyone,
        Still working on figurin' out stuff
        Like why is life so hard
        And why I've gotta walk so far
        For a slice of pizza
        """

# # enclose the poem with ------------------ and print the poem
print(f"---------------------------\n {poem} \n---------------------------")

# create a variable five where you're storing a value of 5 after math
five= 10/2+5*1-0+25-20
# define a function secret_formula(started) 
def secret_formula(started):
    # store jelly_beans which mults started by 500 
    jelly_beans= started*500
    # store jars that div jelly_beans by 1000
    jars= jelly_beans/1000
    # store crates that div jars by 100
    crates= jars/100
    # return all the vals
    return jelly_beans, jars, crates

# store 10000 as a start_point
start_point = 10000
# pass beans, jars and crates int the secret formula
beans,jars,crates = secret_formula(start_point)
# print a string formatted start_point
print("starting point is {}".format(start_point))
#print the beans, jars, and crates
print(f"we have beans: {beans}, jars:{jars}, crates:{crates}")
#mutate start_pount by setting it equal to itself div'ed by 10
start_point=start_point/10
#set formula equal to the secret_formula function, pass in start_point
formula= secret_formula(start_point)
# print the list and format it with an argument store
print("We have {} beans, {} jars, {} crates".format(*formula))

