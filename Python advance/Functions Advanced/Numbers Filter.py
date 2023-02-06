def even_odd_filter(**numbers):
    if "odd" in numbers:
        numbers["odd"] = [int(n) for n in numbers["odd"] if n % 2 == 1]
    if "even" in numbers:
        numbers["even"] = [int(n) for n in numbers["even"] if n % 2 == 0]
    return dict(sorted(numbers.items(), key = lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
