# import(s)
import os

# declarations
folderName = "beens"
fileName = folderName + '/' + 'test.txt'

# create the folder (test if exists first!)
if not os.path.exists(folderName):
    os.makedirs(folderName)

# write a file in the folder
file = open(fileName, 'w')
file.write("this is data in the text file")
file.close()
