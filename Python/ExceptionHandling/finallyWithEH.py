try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print(FileNotFoundError)
finally:
    print("This will always execute")