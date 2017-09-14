tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


'''Study Drill

esc_bell="this does\a a thing"                  # cool this thing makes a noise
esc_back="this does\b another thing"            # deletes previous char
esc_form="this \fformthing"                     # puts a box thing next to it
esc_carriag="what's\r a \rcarriage\r missing?"  # return carriage, used with "\r\n"
esc_unicode= "\N{SOLIDUS} \N{BLACK SPADE SUIT}" # prints unicode character a slash and a spade
esc_sixteen_hex ="\u041b"
esc_thirty_two_hex="\U00000011"
esc_vertical = "don't see\vthis everyday"
esc_octal = "\101\102\103" # \ooo is a placeholder for numbers
esc_hex= "\x41\x42\x43"    # more hex values
print(esc_bell)
print(esc_back)
print(esc_form)
print(esc_carriag)
print(esc_unicode)
print(esc_sixteen_hex)
print(esc_thirty_two_hex)
print(esc_hex)
print(esc_vertical)
print(esc_octal)

esc_exercise="""
I\'d find a few of these things on the grocery list
* pizza
* ice creams\b
and will have to remember
\tNOT
\t\tto
\t\t\tsleep
\t\t\t\tin
\t\t\t\t\tthe
\t\t\t\t\t\tfridgerator 
\t\t\t\t\t\t\t\tsection.
"""

print(esc_exercise)
'''