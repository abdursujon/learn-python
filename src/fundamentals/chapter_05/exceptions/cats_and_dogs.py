from pathlib import Path

def write_cat_and_dog_inf(path, name_list):
    with path.open("w", encoding='utf-8') as file:
        for name in name_list:
            file.write(name + "\n")

def read_cat_and_dog_inf(cat_path, dog_path):
    try:
        cat_names = cat_path.read_text(encoding='utf-8').splitlines()
        dog_names = dog_path.read_text(encoding='utf-8').splitlines()
    except FileNotFoundError:
        print(f"File {path} not found")
    else:
        for c in cat_names:
            print(f"{c}")
        for d in dog_names:
            print(f"{d}")

# Test both methods 
file_names = ["../../../data/text_files/cat.txt", "../../../data/text_files/dog.txt"]

cats = ["Mike", "Miki", "Piano", "Violin"]
dogs = ["Jasper", "Timi", "Nosi", "Piku"]
cat_path = Path(file_names[0])
dog_path = Path(file_names[1])
write_cat_and_dog_inf(cat_path, cats)
write_cat_and_dog_inf(dog_path, dogs)

read_cat_and_dog_inf(cat_path, dog_path)