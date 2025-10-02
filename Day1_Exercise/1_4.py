def compare_numbers(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        if num1>num2:
            print(f"{num1} is greater than {num2}")
        elif num1==num2:
            print(f"Both are same as {num1}")
        else:
            print(f"{num1} is smaller than {num2}")
    else:
        print("Both inputs should be integer")

compare_numbers(10,"20")
