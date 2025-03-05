try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print(ZeroDivisionError)
else:
    print("Success! the result is", result)