values = tuple(map(float, input().split(" ")))
counter_of_values = {value: values.count(value) for value in values}

for key, value in counter_of_values.items():
    print(f"{key} - {value} times")