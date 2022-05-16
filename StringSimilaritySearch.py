'''
initial look
Project read a text file and filter it
List of things to do:
read file
use regex

-read csv
-print as a table


'''
import re

file = open('hello.txt','r')
for x in file:
    x = re.sub("[^a-zA-Z\d\s:]+"," ",x)
    print(x)

