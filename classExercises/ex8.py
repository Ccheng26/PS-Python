formatter= "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    #first 4 lines of T.S.Eliot's The Waste Land
    "April is the cruellest month, breeding",
    "Lilacs out of the dead land, mixing",
    "Memory and desire, stirring",
    "Dull roots with spring rain."
))