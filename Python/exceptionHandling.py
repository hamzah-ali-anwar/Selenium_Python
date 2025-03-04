number = input("Please enter the number: ")
print(f"Multiplication table of {number} is: ")

try:
    for i in range(1, 11):
        print(f"{int(number)} X {i} = {int(number) * i}")
except:
    print("Invalid Input!")

print("Some imp lines of codes")
print("End of program")