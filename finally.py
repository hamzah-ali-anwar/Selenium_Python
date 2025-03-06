try:
    l = [1, 2, 3, 4]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occured")

finally:
    print("I always get executed")