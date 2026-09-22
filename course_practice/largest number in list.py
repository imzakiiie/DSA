numbers = [21,42,49,93,89]
largest = numbers[0]
for element in numbers[1:]:
    if element > largest:
        largest = element
print(f"largest element : {largest}")