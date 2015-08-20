#a=int(input())#never use input() if import os;os.system('do something bad')
#http://stackoverflow.com/questions/1588058/python-read-two-variables-in-a-single-line
#b=input()
#print(a)
import sys
a,b = map(int, raw_input().split())
#raw_input is in python 2 and input in python 3. The differnce is raw_input reads input as a string but input reads input as python expressions
print a,b
