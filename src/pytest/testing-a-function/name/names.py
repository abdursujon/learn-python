from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True: 
    first = input("\nEnter First Name: ")
    if first == 'q': 
        break
    last = input("\nEnter Last Name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\nFormatted name: {formatted_name}")