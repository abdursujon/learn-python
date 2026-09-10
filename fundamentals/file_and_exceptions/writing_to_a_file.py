from pathlib import Path 

path = Path('../../data/programming.txt')
contents = ["I love Java\n", "I love Python\n", "I love coding\n", "I love building new things\n", "I love solving problems\n"]
full_text = "".join([str(item) for item in contents])
path.write_text(full_text)

# This section of the code writes to a file without overwriting existing data 
path_two = Path('../../data/user.txt')
while True: 
    print("Enter 'q' to quit anytime.")
    response = input("What is your name?")
    if response == 'q':
        break
    else:
        # With automatically closes the file even if error occurs. utf-8 ensures the file stores text in a universal format 
        with path_two.open("a", encoding="utf-8") as file: 
            file.write(response + "\n")

