from pathlib import Path
import json

# We use json.dumps() to write to a file in json format. 
n = 1
square_numbers = []
while(n <= 10):
    square_numbers.append(n * n)
    n += 1

path = Path('../../../data/json/square_numbers.json')
contents = json.dumps(square_numbers)
path.write_text(contents)

# We can use json.loads() to read from the json file we have just written. 
read_square_num = path.read_text()
numbers = json.loads(read_square_num)
print(numbers)