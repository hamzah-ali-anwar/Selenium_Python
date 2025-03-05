# Exception handling in Python is done using try, except, else, and finally blocks to catch and handle errors gracefully.

try:
    x = 10 / 0
except zeroDivisionError:
    print("Integer can't be divided by zero")