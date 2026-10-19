# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)

from artworks import artworks

counts = {}

for i in range(len(artworks)):
    art = artworks[i].get('artist', 'Unknown')
    if art not in counts:
        counts[art] = counts.get(art, 0) + 1
    else:
        counts[art] += 1

        
print(counts)

most = 0
most_artist = ""

for artist in counts:
    if counts[artist] > most:
        most = counts[artist]
        most_artist = artist

print(f"Most works: {most_artist} ({most})")