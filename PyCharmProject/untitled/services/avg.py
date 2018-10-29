def average(numbers):
    total = 0
    for num in numbers:
        total = total + num

    avg = total / len(numbers)
    return avg

cnt = 10000