from collections import deque

bowls_of_ramen = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while True:
    if not bowls_of_ramen or not customers:
        break

    current_bowl = bowls_of_ramen.pop()
    current_customer = customers.popleft()

    if current_customer == current_bowl:
        continue
    elif current_customer > current_bowl:
        current_customer -= current_bowl
        customers.appendleft(current_customer)
    elif current_bowl > current_customer:
        current_bowl -= current_customer
        bowls_of_ramen.append(current_bowl)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")