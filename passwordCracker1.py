# Find and open the password file
#  <your code goes here>

# Identify users whose password is the same as their username
# <your code goes here>

# Print the list

#Kenneth Chan Assignment 3 PasswordCrack1

import sys
import hash

fileName = sys.argv[1]

hashedPwds = open(fileName).readlines()
for line in hashedPwds:
    l = line.split(':')
    username = l[0]
    hashedUsername = hash.hash(username)
    hashedPassword = l[1].strip('\n')

    if hashedUsername == hashedPassword:
        print(username)

#done
