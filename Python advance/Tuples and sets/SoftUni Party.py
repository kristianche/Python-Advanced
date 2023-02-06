number_of_guests = int(input())
guests = set(input() for _ in range(number_of_guests))
vip_guests_reservation = []
normal_guests_reservation = []

for guest_reservation in guests:
    if guest_reservation[0].isdigit():
        vip_guests_reservation.append(guest_reservation)
    else:
        normal_guests_reservation.append(guest_reservation)

while True:
    name = input()
    if name == "END":
        break
    else:
        if name in vip_guests_reservation:
            vip_guests_reservation.remove(name)
        elif name in normal_guests_reservation:
            normal_guests_reservation.remove(name)

print(int(len(vip_guests_reservation)) + int(len(normal_guests_reservation)))
for guest in sorted(vip_guests_reservation):
    print(guest)
for guest in sorted(normal_guests_reservation):
    print(guest)
