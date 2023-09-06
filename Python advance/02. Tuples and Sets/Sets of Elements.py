n, m = [int(x) for x in input().split(" ")]

first_set = {int(input()) for _ in range(n)}
second_set = {int(input()) for _ in range(m)}
final_set = first_set.intersection(second_set)

for element in final_set:
    print(element)