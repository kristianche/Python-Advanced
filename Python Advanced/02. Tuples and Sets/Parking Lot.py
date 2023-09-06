plate_number_record = [input() for _ in range(int(input()))]
parking = set()
command_IN = "IN"
command_OUT = "OUT"

for record in plate_number_record:
    command, car_number = record.split(", ")
    if command == command_IN:
        parking.add(car_number)
    elif command == command_OUT:
        parking.remove(car_number)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")
