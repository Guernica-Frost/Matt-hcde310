# HW2 Part 2 – One dict = one thing
#
# In `part2.py`, print each artwork as `Title - Artist (Year)`, for example `The Bedroom - Vincent van
# Gogh (1889)`. Use `.get()` so a missing artist or year prints `Unknown` instead of crashing.

from artworks import artworks
for i in range(len(artworks)):
    print(f"{artworks[i].get('title')} - {artworks[i].get('artist', 'Unknown')} ({artworks[i].get('year', 'Unknown')})")
