longest_intersection = set()
n = int(input())

for _ in range(n):
    first_data, second_data = [el.split(",") for el in input().split("-")]

    first_set = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))

    current_set_intersection = first_set.intersection(second_set)

    if len(current_set_intersection) > len(longest_intersection):
        longest_intersection = current_set_intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with "
      f"length {len(longest_intersection)}"
      )