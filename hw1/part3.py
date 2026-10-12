# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"

i = 0

for title in titles:
    if years[i] >= cutoff:
        print(title)
    i+=1

print()

i = 0
old = 0
modern = 0

for title in titles:
    if years[i] < cutoff:
        print(f"{title}: old")
        old += 1
    else:
        print(f"{title}: modern")
        modern += 1

    i += 1

print()

print(f"Old: {old}")
print(f"Modern: {modern}")

