#!python3

'''
Ask the user to enter in a list of 5 words.
Convert the word to a string literal JSON object
Write the contents to a file called 'task3.txt'

Example:
Enter a word: frog
Enter a word: french
Enter a word: puppy
Enter a word: escalate
Enter a word: ice

task3.txt contents:
["frog","french","puppy","escalate","ice"]

'''
import json

a = input("Enter a word: ")
b = input("Enter a word: ")
c = input("Enter a word: ")
d = input("Enter a word: ")
e = input("Enter a word: ")

alist = [a,b,c,d,e]
file = open("task3.txt", "w")
new = json.dumps(alist)
new = str(new)
file.write(new)