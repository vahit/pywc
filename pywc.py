#!/usr/bin/python3.3

## Filename: pywc.py
##           A simple wc like script witch use an another algorithm for counting words.
## Feedback: Vahid.Maani [at] gamil [dot] com

## import needed modules.
import sys
import random

## Check an argumnts and print usage.
if len(sys.argv) < 2 :
    print("You need to specify a file name:")
    print(sys.argv[0], "<path/filename>")
    sys.exit()

file_read = open(sys.argv[1])
file_contents = list(file_read.read())

word_count = 0
line_count = 0
x = 0
word = ""

## Check all character one by one and count words.
while x < len(file_contents):
    if file_contents[x].isalpha():
        word += file_contents[x]
        x += 1
        continue
    elif word != "":
        word_count += 1
        word = ""
        x += 1
    else:
        x += 1

## Check all characters on by one again and count new lines.
for x in range(0,len(file_contents)):
    if file_contents[x] == "\n":
        line_count += 1

## Count characters with "len(file_contents)" command.
print("\t", line_count,"\t", word_count, "\t", len(file_contents))
