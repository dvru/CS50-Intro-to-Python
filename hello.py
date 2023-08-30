# Ask user for their name and Removes whitespace from str and capilative user's name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {name}")



