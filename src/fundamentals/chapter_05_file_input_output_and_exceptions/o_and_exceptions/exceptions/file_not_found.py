from pathlib import Path 
path = Path('../../../data/text_files/mike.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry the file {path} does not exists.")
