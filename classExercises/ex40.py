#creating class Song
class Song(object):
    # initializing object with lyrics
    def __init__(self,lyrics):
        self.lyrics= lyrics
    # defining function in Song
    def sing_me_a_song(self):
        # calls lyrics, and iterates through lines
        for line in self.lyrics:
            # prints the lines
            print(line)
# instantiating objects
happy_bday= Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right here"])
bulls_on_parade= Song(["They rally around the family",
                       "With pockets full of shells"])
# calling object methods
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()