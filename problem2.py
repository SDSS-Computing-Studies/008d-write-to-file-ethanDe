##### Problem 2
"""Write a program to keep track of your current grades for 8 subjects.  Create a menu system that lets a user do the following:
1. Change the name of their subjects
2. Enter in a new value for their grade
3. Read data from a file
4. Save the current data to a file.
"""

import json
def subject():
    a = input("Enter subject a: ")
    b = input("Enter subject b: ")
    c = input("Enter subject c: ")
    d = input("Enter subject d: ")
    e = input("Enter subject e: ")

    alist = [a + ": 95",b + ": 95",c + ": 95",d + ": 95",e + ": 95"]
    file = open("problem2.txt", "w")
    new = json.dumps(alist)
    new = str(new)s
    file.write(new)


def display():
    file = open("problem2.txt","r")
    d = file.read()
    print(f"Your courses:\n\n{d} \n")

def interact():
    
subject()
display()
#jsonloads