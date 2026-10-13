# Class 4: Five broken snippets

Your name: Matt Shi
Collaborator: Yuyao Sun

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks?
Line 8
- What error will Python show? (the kind and the message)
KeyError, No such key in dictionary
- What's the fix?
change the key "Room" to "room"


## Snippet 2
- Which line breaks?
Line 12
- What error will Python show? (the kind and the message)
TypeError, can only contanate str not int
- What's the fix?
print(f"'Find it in room: ' {exhibit['room']}")

## Snippet 3
- Which line breaks?
Line 17
- What error will Python show? (the kind and the message)
IndexError, index out of range
- What's the fix?
for i in range(len(exhibits)): , don't plus 1 in range()

## Snippet 4
- Which line breaks?
Line 29
- What error will Python show? (the kind and the message)
NameError, visit is not defined.
- What's the fix?
change visit in Line 29 into visits

## Snippet 5
- Which line breaks?
Line 41
- What error will Python show? (the kind and the message)
OutputError, no return in the functions
- What's the fix?


# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke?
line 
- What error did Python show?
KeyError: 'Room'
- What's the fix?
change 'Room' into 'room'

## Snippet 2
- Which line broke?
line 12
- What error did Python show?
TypeError: can only concatenate str (not "int") to str
- What's the fix?
print(f"'Find it in room: ' {exhibit['room']}")

## Snippet 3
- Which line broke?
line 17
- What error did Python show?
IndexError: list index out of range
- What's the fix?
for i in range(len(exhibits)): , don't plus 1 in range()

## Snippet 4
- Which line broke?
line 29
- What error did Python show?
NameError: name 'visit' is not defined
- What's the fix?
change visit in Line 29 into visits

## Snippet 5
- Which line broke?
line 41
- What error did Python show?
AttributeError: 'NoneType' object has no attribute 'upper'
- What's the fix?
change the print statement into return statement

When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #:5
- Our guess before asking: output error, because there's no return statement in the function. The function won't return anything which means varaible title is void.
- Chat:
AI tutor (Codex): In Snippet 5, the function uses print(longest) instead of return longest. print() displays the title, but it does not send that value back to the caller. Since the function has no return statement, it automatically returns None, so title becomes None.
When Python reaches print(title.upper()), it raises AttributeError: 'NoneType' object has no attribute 'upper' because None does not have an .upper() method.
To fix this, replace print(longest) with return longest. Then title receives "Water Lilies", and the final line prints WATER LILIES. This also explains why the original code prints Water Lilies before crashing: the function prints it, but still returns None.
- Did it give you too much? What did you do?
I feel it its alright to me. 
No, it gave me the right amount of detail. The explanation helped me understand why the function printed the title but still returned None. After reading, I understood why replacing print(longest) with return longest solves the error.

