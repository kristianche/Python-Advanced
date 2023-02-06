from collections import deque

milligrams_of_caffeine = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))

stamat_caffeine = 0

while True:
    if not milligrams_of_caffeine or not energy_drinks:
        break
    current_caffeine = milligrams_of_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    caffeine_quantity = current_caffeine * current_energy_drink
    total_caffeine = stamat_caffeine + caffeine_quantity

    if total_caffeine > 300:
        if stamat_caffeine >= 30:
            stamat_caffeine -= 30
        energy_drinks.append(current_energy_drink)
    elif total_caffeine <= 300:
        stamat_caffeine += caffeine_quantity


if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")
