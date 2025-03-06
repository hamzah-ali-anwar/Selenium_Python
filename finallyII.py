def func1():
    try:
        l = [1, 2, 3, 4]
        i = int(input("Enter an index: "))
        print(l[i])
        return f"success, index {i} exist"
    except:
        print("Some error occured")
        return f"failure, index {i} doesn't exist"
    
    finally:
        print("I'm always executed")

x = func1()
print(x)