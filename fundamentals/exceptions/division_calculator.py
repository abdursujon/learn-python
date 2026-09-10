print("Provide two number, for division.")
print("Enter 'q' to quit")

while True: 
    num_1 = input("Enter first number: ")
    if num_1 == 'q':
        break

    num_2 = input("Enter second number: ")
    if num_2 == 'q':
        break

    # The only code that should go on try is the code that might through an exception    
    try:
        div = int(num_1) / int(num_2)
    except ZeroDivisionError:
        print("You can't divide a number by zero! Zero is nothing remember.")
    else:
        print(f"Division is {div}")