print("Mary had a little lamb.")
#puts the argument snow into the reseved {} and prints it
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
#prints the . 10 times
print("." * 10) #what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
#the comma prints a space between the two variables and concatinates it with the next line
print(end7 + end8 + end9 + end10 + end11 + end12)

#interestingly enough 
# print(end1 + end2 + end3 + end4 + end5 + end6 + end = ' ') does not work
# end is a keyword that prints the value at the end of what you wanted to print
# it cannot be evaluated as an expression which is why it doesn't play nicely with the + sign, it's assuming we want to evaluate what's being done to end
# in this case we are reassigning the value of the keyword to an empty space instead of the default new line
