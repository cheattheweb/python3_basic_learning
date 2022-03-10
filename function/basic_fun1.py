from cgi import print_directory
from distutils.core import run_setup
from termios import NL1
from unittest import result

from numpy import number


def add(x, y):# parameters
    return x + y;

n = input("Enter the 1st value: ")
m = input("Enter the 2nd value: ")
n = int(n)
m = int(m)
result= add(n, m)#arguments
print(result)

number1 = input("Enter the 1st value: ")
number2 = input("Enter the 2nd value: ")
number1 = int(number1)
number2 = int(number2)
result = add(number1, number2)#arguments
print(result)

print(add(2.6, 3.5))
