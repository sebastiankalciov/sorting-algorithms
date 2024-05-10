
import random

def generate_numbers(file, min_number, max_number, size):
    with open(file, "w") as f:
        for _ in range(size):
            f.write(f"{random.randrange(min_number, max_number)}\n")

    print("numbers generated successfully")


generate_numbers("data/ten_mil_numbers.txt", 1, 10000000, 10000000)