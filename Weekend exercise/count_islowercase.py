text = input("Enter your string: ")

count = 0

for letter in text:
    if letter.islower():
        count +=1
print("Your lowercase letters are: ", count)
