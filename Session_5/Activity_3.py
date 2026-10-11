n = int(input("Enter a number: "))

square_dictionary = {}

for i in range(1, n + 1):
    square = i * i
    square_dictionary[i] = square

print(square_dictionary)
