# pathlib is a module of python which consist of Path class which we can use to read from a file 
from pathlib import Path 

path = Path('../data/pi_digits.txt')
content = path.read_text().rstrip() # remove extra blank line after output as read_text() creates empty string after finish reading 
lines = content.splitlines() # a list of all line from read file 
pi_string = ""
for line in lines: 
    # strip extra space on left 
    pi_string += line.lstrip().replace(' ', '')
print(pi_string)


path_two = Path('../data/pi_million_digits.txt')
content_two = path_two.read_text().rstrip()
lines_two = content_two.splitlines()
pi_string_two = ""
for line in lines_two:
    pi_string_two += line.lstrip().replace(' ', '')
print(f"{pi_string_two[:1000]}...")

# Check if your birthday is in the string of one_million_string 
birthday = input("Enter your birthday in the form of mmddyy: ")
birthday_counter = []
# find how many times your birthday appears in first one million digits of pi 
start = 0 
while True: 
    index = pi_string_two.find(birthday, start) # find the first index where birthday is found
    if index == -1:
        break
    birthday_counter.append(index)
    start = index + 1 # since we alreaydy counted the index we got, now we make sure we move on to next after the index   

if birthday_counter:
    print(f"Your birthday appears {len(birthday_counter)} times in the first million digits of pi")
    if(len(birthday_counter) > 10):
        print(f"At positions: {birthday_counter[:10]}...")
    if(len(birthday_counter) > 1 and len(birthday_counter) <= 10):
        print(f"At positions: {birthday_counter}")
    else:
        print(f"At position: {birthday_counter[0]}")
else:
    print("Opps, sorry you birthday do not appear in the first million digits of pi")
