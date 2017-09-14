# Find and open the password file and dictionary file
#  <your code goes here>

# Identify users whose password appears in the dictionary file
# <your code goes here>

# Print the list

#Kenneth Chan Assignment 3 PasswordCrack2

import sys
import hash

fileName = sys.argv[1]
file2Name = sys.argv[2]

hashedPwds = open(fileName).readlines()
dictionaryWords = open(file2Name).readlines()

#create array to print matches
finalList = []

for word in dictionaryWords:
        word = word.strip('\n')
        hashedWord = hash.hash(word)
        for line in hashedPwds:
            l = line.split(':')
            username = l[0]
            hashedPassword = l[1].strip('\n')
            if hashedWord == hashedPassword:
               finalList.append(l[0] + ':' + word)

for a in finalList:
    print (a)

#done
