from collections import deque
conquered_peaks = ["Musala", "Vihren", "Shipka"]
n = '\n'
print(f"Conquered_peaks: {n}{n.join(conquered_peaks)}")

print("\n".join(['I', 'would', 'expect', 'multiple', 'lines']))
peaks = deque([
    "Musala",
    "Vihren"
])
current_peak = peaks.copy().popleft()
print(current_peak)