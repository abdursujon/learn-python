from pathlib import Path 
path_three = Path('../../../data/text_files/user.txt')

# "r" = read, "a" = append, "w" = write 
while True:
    print(f"Type 'y' for Yes | Type 'n' for No | Type 'q' to quit\n")
    response = input("Do you wish to clear your data?")
    if response == 'q':
        break
    if response == 'n':
        continue
    if response == 'y':
        with path_three.open("w") as file:
            print("Your data has been clear")
            pass
        break