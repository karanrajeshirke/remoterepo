# Function to calculate the square of numbers in a list
def square_numbers(numbers):
    return [num ** 2 for num in numbers]

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate squares
squares = square_numbers(numbers)

# Print results using string formatting
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squares}")

# Simple loop to demonstrate iteration
for num in numbers:
    print(f"The square of {num} is {num ** 2}")
