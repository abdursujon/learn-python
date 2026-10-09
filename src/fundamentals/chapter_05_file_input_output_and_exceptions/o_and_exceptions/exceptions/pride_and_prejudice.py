from pathlib import Path 

''' 
We have downloaded the free txt file that consist of entire pride and prejudice
book which we will utilise to do some interesting things with python.
'''

path = Path('../../../data/text_files/pride_and_prejudice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Looks like file: {path} does not exists.")
else:
    words = contents.split()
    print(f"The file: {path} has about {len(words)} words!")
    
    # Let's check how many times the word "pride" and "prejudice" appears on the book 
    pride_counter = 0
    prejudice_counter = 0
    for word in words: 
        if word == 'pride':
            pride_counter += 1
        if word == 'prejudice':
            prejudice_counter += 1
        else:
            continue
    print(f"The wrod 'pride' appears {pride_counter} times in the 'Pride and Prejudice' book")
    print(f"The wrod 'prejudice' appears {prejudice_counter} times in the 'Pride and Prejudice' book")