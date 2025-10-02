def compare_int_and_str(num1, num2):
    if not isinstance(num1,int):
        print("Error: The first value should be an integer")
        return

    if not isinstance(num2, str):
        print("Error: The second value should be string")
        return


    try:
        num2_int=int(num2)
    except ValueError:
        print("Error: The second parameter should be a string that can be converted to an integer.")
        return


    if num1 == num2_int:
        print(f"{num1} and {num2} represent the same value.")
    else:
        print(f"{num1} and {num2} do not represent the same value.")



compare_int_and_str(12,"24.5")
