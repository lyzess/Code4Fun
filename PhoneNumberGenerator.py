import random

# Function to generate random 11-digit numbers starting with '011'
def generate_numbers(num_count):
    numbers = []
    for _ in range(num_count):
        # Generate random 8 digits after '011'
        random_digits = random.randint(10000000, 99999999)
        # Prepend '011' to the random digits
        number = f"017-{random_digits}"
        numbers.append(number)
    return numbers

# Generate 200 numbers
random_numbers = generate_numbers(200)

# Print the numbers
for number in random_numbers:
    print(number)