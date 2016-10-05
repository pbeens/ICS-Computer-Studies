'''
Sometimes in class you will be asked to put the output from your program in a personalized subfolder, perhaps named
with your name or your initials.

This example shows you how you can create the folder, as well as delete the folder and its contents if it already exists.
'''

# import(s)
import os
import shutil

# declarations
folderName = "beens"

# delete the folder and its contents if it aleady exists
if os.path.exists(folderName):
    shutil.rmtree(folderName)

# create the folder
os.makedirs(folderName)

# write a file in the folder
fileName = 'test.txt'
file = open(folderName + '/' + fileName, 'w')
file.write("this is data in the text file")
file.close()
