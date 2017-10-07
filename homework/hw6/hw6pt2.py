# 3. Write a code that prints out 15 most frequent from the file words.txt. 

# open file, and read text.txt
text = open("text.txt","r")
# initialize dictionary
word_count = dict()

import string
import re
# iterates through content in textfile
for line in text:
    # split line on spaces and removes punctuation
    # iterates through line, checks raw string deletes whitespaces using sub(substitute), deletes line breaks using replace, and splits on remaining spaces to form list
    words = re.sub(r'[^\w\s]','',line).replace("\n","").split(" ")
    # iterates through list of words with whitespace stripped
    for word in words:
        # checks if word is in dictionary, if not present, add first occurance
        # also does a check for words, length must be >0
        if word in word_count and len(word)>0:
            word_count[word]+=1
        elif len(word)>0:
            word_count[word]= 1

# get the dictionary word count values, sort them by highest to lowest (reverse=True), limit range to 15
freq_nums=sorted(word_count.values(),reverse=True)[0:15]
# iterates through word_count dictionary, prints word if value is matched to the 15 values noted in list above
for most_word in word_count:
    if(word_count[most_word] in freq_nums):
        print([most_word][0])
