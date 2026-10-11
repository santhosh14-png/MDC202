result = []

for number in range(2000, 3201):
    if number % 7 == 0 and number % 3 != 0:
        result.append(number)

print(result)

