try:
    num = int(input("Enter an integer: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Invalid input! please enter a valid number")
except ZeroDivisionError:
    print("Erro: Number can't be divided by zero")