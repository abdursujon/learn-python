from pathlib import Path 

''' We can use the keyword pass on except block to tell python if a failure happens, just ignore it and not report anything'''
def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else: 
        words = contents.split()
        print(f"The file: '{path}' has about {len(words)} words!")

# here alice.txt does not exist and we do not report anything we continue to the next files 
file_names = ["../../../data/text_files/pi_digits.txt", "../../../data/text_files/pi_million_digits.txt", 
              "../../../data/text_files/alice.txt", "../../../data/text_files/pride_and_prejudice.txt", "../../../data/text_files/user.txt"] 
for file in file_names:
    path = Path(file)
    count_words(path)