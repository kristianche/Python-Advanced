numbers = [int(x) for x in input().split(" ")]
positive_numbers = [int(x) for x in numbers if x > 0]
negative_numbers = [int(x) for x in numbers if x < 0]

positive_numbers_sum = sum(positive_numbers)
negative_numbers_sum = sum(negative_numbers)

print(negative_numbers_sum)
print(positive_numbers_sum)

if abs(negative_numbers_sum) > abs(positive_numbers_sum):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


