print("How many live cables must I avoid?")
live_cables = int(input())
live_cabled = 0
print()
while live_cabled < live_cables:
    print("Avoiding...", end="")
    live_cabled += 1
    print(f"done! {live_cabled} life cables avoided.")

print("all lives cable avoided")