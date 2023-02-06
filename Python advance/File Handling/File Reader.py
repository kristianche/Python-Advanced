def numbers_sum(file_name):
    data = open(file_name, "r")
    sum = 0

    for num in data:
        sum += int(num)

    return sum


print(numbers_sum("numbers.txt"))