user_input = input("Enter characters separated by commas: ")


result = ""

for character in user_input:
    if character != ",":
        result += character

print(result)
