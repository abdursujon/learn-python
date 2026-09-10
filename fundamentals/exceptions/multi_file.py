from pathlib import Path 
'''This file shows how to deal with multiple file with proper exception handling'''

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Looks like file: '{path}' does not exists.")
    else: 
        words = contents.split()
        print(f"The file: '{path}' has about {len(words)} words!")

file_names = ["../../data/text_files/pi_digits.txt", "../../data/text_files/pi_million_digits.txt", 
              "../../data/text_files/alice.txt", "../../data/pride_and_prejudice.txt", "../../data/text_files/user.txt"] 
              
for file in file_names:
    path = Path(file)
    count_words(path)