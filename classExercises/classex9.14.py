# ask users for two files as arguments
# read the content of the first file
# write the content of the first file to the 2nd file
# HINT: you can save the content to a variable...

from sys import argv

script, readFile, writeFile=argv
getFile = input(readFile)
openFile = open(readFile)

target = open(writeFile, 'w')
target.write(f"{openFile.read()}")
openFile.close()

''' class notes
# step 1: import argv
from sys import argv
# step 2: create variables for arguments
script, file1, file2 = argv
# step 3: open(file that has to be readd)
# step 4: create a variable for open file
read_file = open(file)
# step 5: read this file
# step 6: hold it in a variable
content= read_file.read()
print(content)
# step 7: open 2nd file with write permission
write_file=open(file2,'w')
# step 8: write into 2nd file
write_file.write(content)
# step 9: close the first file
read_file.close()
# step 10: close the second file
write_file.close()
'''