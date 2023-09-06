from collections import deque


portion_quantity = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))
conquered_peaks = []
peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])
day = 1
while True:
    if day > 7 or not portion_quantity or not stamina or len(conquered_peaks) == 5:
        break

    current_portion = int(portion_quantity.pop())
    current_stamina = int(stamina.popleft())
    energy = current_stamina + current_portion
    copy = peaks.copy()
    current_peak = copy.popleft()
    if energy >= current_peak[1]:
        name = current_peak[0]
        conquered_peaks.append(name)
        peaks.popleft()
    day += 1

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    if conquered_peaks:
        print("Conquered peaks:")
        for peak in conquered_peaks:
            print(peak)
elif len(conquered_peaks) < 5:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    if conquered_peaks:
        print("Conquered peaks:")
        for peak in conquered_peaks:
            print(peak)










