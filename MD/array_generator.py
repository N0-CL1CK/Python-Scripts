from random import randint

arrays_length = [length for length in range(2*10**4, (10**5)+1, 2*10**4)]
array = []

for length in arrays_length:
    array.clear()
    for i in range(length):
        next = False
        while not next:
            random_number = randint(0, 10**5)
            if random_number not in array:
                array.append(random_number)
                next = True

    with open(f"array_with_{length}_elements.txt", "w") as file:
        file.write(f"{array}\n")