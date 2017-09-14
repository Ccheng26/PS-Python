from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

'''Study Drill
#Zork and Adventure is a text based adventure games with prompts requesting the user to do actions

script, user_name, language = argv
filler = '****'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Is your first name {user_name}?")
likes = input(filler)

print(f"Who gave named you {user_name}?")
lives = input(filler)

print("What kind of computer do you have?")
computer = input(filler)

print(f"Do you use that computer to program with {language}?")

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You have a {computer} computer.
AND you know {language}, how cool is that?!
""")
'''