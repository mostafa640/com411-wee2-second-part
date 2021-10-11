print("How many bars should be charged?")
bars_charge = int(input())
bar_charged = 0
print()
while bar_charged < bars_charge:
    bar_charged += 1
    print(f"charging: { '█' * bar_charged}")

print("battery is full")

