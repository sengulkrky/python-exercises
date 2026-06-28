numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# print sum of numbers
print(f"Sum: {sum(numbers)}")

# print max
print(f"Max: {max(numbers)}")

# print min
print(f"Min: {min(numbers)}")

# print unique numbers as array
print(f"Unique numbers: {set(numbers)}")

# print unique numbers as string
print(f"Unique numbers: {', '.join(str(n) for n in sorted(set(numbers)))}")