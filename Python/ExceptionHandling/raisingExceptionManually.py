def check_age(age):
    if age < 18:
        raise ValueError("You must be 18 or older")
    return "Access granted"

try:
    print(check_age(16))
except ValueError as e:
    print(f"Exception caught: {e}")