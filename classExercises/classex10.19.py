# traverse throrugh the following string using a while loop "Purple banana" and print out each letter at a time

in_string= 'Purple banana'
counter = 0
string_= list(in_string)


while(counter<len(string_)):
    print(string_[counter])
    counter+=1

while(counter<len(in_string)):
    print(in_string[counter])
    counter+=1

# for i in string_:
#     print(i)

'''
# find the length of a string provided by the user without using the built in length function
# stores length
counter = 0
# takes input
given= input('>')
# iterate through input
for i in given:
    # increments on length while iterating through string
    counter+=1
print(counter)
'''