from collections import deque

textiles = deque(int(i) for i in input().split(" "))
medicaments = [int(i) for i in input().split(" ")]
items = {}


while True:
    if not medicaments or not textiles:
        break

    current_textile = int(textiles.popleft())
    current_medicament = int(medicaments.pop())
    resource = current_medicament + current_textile

    if resource == 30:
        item = "Patch"
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1
    elif resource == 40:
        item = "Bandage"
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1
    elif resource == 100:
        item = "MedKit"
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1
    elif resource > 100:
        item = "MedKit"
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1
        remaining = resource - 100
        medicaments[-1] += remaining
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

sorted_items = sorted(items.items(), key= lambda x: (-x[1], x[0]))
if textiles and not medicaments:
    print("Medicaments are empty.")
    for key, value in sorted_items:
        print(f"{key} - {value}")
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
elif not textiles and medicaments:
    print("Textiles are empty.")
    for key, value in sorted_items:
        print(f"{key} - {value}")
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments[::-1]])}")
elif not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
    for key, value in sorted_items:
        print(f"{key} - {value}")