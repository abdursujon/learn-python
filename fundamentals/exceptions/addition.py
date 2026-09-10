while True:
    num_1 = input("Type a number: ")
    num_2 = input("Type a second number: ")
      
    try:
        add = int(num_1 + num_2)
    except ValueError:
        print("Not a number or invalid type given")
    else:
        print(add)
