text = input("Enter a word: ")

count = 0

for letter in text:
    if letter.isupper():
        count += 1
print("Your uppercase letters are: ", count)
