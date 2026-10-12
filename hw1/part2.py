# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles

count = 0
longest = ""
i = 1

for title in titles:
    print(f"{i}. {title}")
    i += 1

    if "a" in title.lower():
        count += 1

    if len(title) > len(longest):
        longest = title

print(f"Titles: {len(titles)}")
print(f'Titles with an "a": {count}')
print(f"Longest: {longest}")