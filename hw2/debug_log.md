# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
*copy it exactly*
NameError: name 'artist' is not defined

### 2. What I thought it meant
Maybe some of the values in dictionary does not have a value of artist.

### 3. What it actually meant
Because I used the wrong quotation mark. I used the single pair instead of double pair.

### 4. The fix
Use art = artworks[i]["artist"]. Thought it still not works because of the error in entry 2.

## Entry 2

### 1. Error message
*copy it exactly*
KeyError: 'Vincent van Gogh'


### 2. What I thought it meant
Probably when list 'counts' wants to add element, python grab the wrong key value. 

### 3. What it actually meant
counts[art] += 1 wants to get the existing value before adding 1, but that key value haven't been added into list yet.

### 4. The fix
I replace counts[art] += 1 with counts[art] = counts[art].get(art, 0) + 1, so a new artist starts with a 0 count before adding 1.
