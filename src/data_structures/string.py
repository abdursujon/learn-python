my_name = " abdur rahim Sujon "

# 1. upper(): convert to uppercase
print(my_name.upper())

# 2. lower(): convert to lowercase
print(my_name.lower())

# 3. capitalize(): capitalize first char only
print(my_name.capitalize())

# 4. title(): capitalize first char of each word
print(my_name.title())

# 5. swapcase(): swap upper/lower case
print(my_name.swapcase())

# 6. strip(): remove leading/trailing whitespace
print(my_name.strip())

# 7. replace(): replace a substring
print(my_name.replace("Sujon", "Suja"))

# 8. split(): split into a list by separator
print(my_name.split(" "))

# 9. join(): join a list into a string
my_name_word_list = ["Abdur", "Rahim", "Sujon"]
print(" ".join(my_name_word_list))

# 10. find(): return index of first occurrence (-1 if not found)
print(my_name.find("Su"))

# 11. index(): same as find() but raises error if not found
print(my_name.index("Su"))
# error: print(my_name.index("Sujonn"))

# 12. count(): count occurrences of a substring
print(my_name.count("Su"))

# 13. startswith() / endswith(): check prefix/suffix
if(my_name.startswith(" abdur") == True):
    print("correct name")

if(my_name.endswith("Sujon ") == True):
    print("correct name")

# 14. isalpha() / isdigit() / isalnum(): check string type
my_name = "Sujon"
age = "24"
print(my_name.isalpha())
print(my_name.isalnum()) # all chars are letters or digits
print(age.isdigit()) 

# 15. isupper() / islower() / isspace(): check case/whitespace
print("ABDUR".isupper())
print("abdur".islower())
print(" ".isspace())

# 16. center() / ljust() / rjust(): padding
my_name = "Abdur Rahim Sujon"
print(my_name.center(200))
my_name = my_name.center(100)
print(my_name.ljust(50)) # hi........
print(my_name.rjust(300)) # ........hi

# 17. zfill(): pad with zeros 
print("10".zfill(4))

# 18. partition(":") splits at the first : and returns a tuple of 3 parts: (before, separator, after).
print("name-sujon:age-24:hobby-football".partition(":"))

# 19. expandtabs(): replace tabs with spaces
print("row1\trow2\trow3")
print("row1\trow2\trow3".expandtabs(1))

# 20. casefold(): aggressive lowercase (for caseless comparison)
hobbies = ["Football", "FOOTBALL"]
print(f"{hobbies[0].casefold()}")
print(hobbies[0].casefold() == hobbies[1].casefold())

# 21. len(): length of the string   
print(len(my_name))