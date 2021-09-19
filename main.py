#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

passage_name = "West of House"
passage_text = "This is an open field west of a white house, with a boarded front door."

#when given "West of House" str value evaluates to passage_text value,  when given "North of House" returns str "Good job!"


print("You are at the " + passage_name)
print(passage_text)
choice = input("What would you like to do?")
if choice == " go north" :
  print("Good job!")
else:
  print("Nope, go back!")




