# HW1 notes

## Part 4: Predict, run, explain

**My prediction for `predict.py` (written BEFORE running it):**
My prediction:
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11


**What it actually printed:**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11


**Explain:** If I was off, which line surprised me and why? If I was right, why do the last two lines print different numbers?
Because print(len(titles)) is actually printing the length of the list "titles". 
This line print(len(titles[0])) is printing the length of the first element in the list "titles", which is the length of string "The Bedroom" that is 11.

## Part 5: Reflection (about 100 words)

Look back at your Day 1 app: its code if you can still open it, or your screenshots of it running. Is there anything you can now recognize (a loop, an `if`, a list)? Where? If you only have screenshots, what do you think the code had to do to make the app behave that way?
After week 2, I can recognize some of the codes in my Day 1 app. The FLOORS array stores the floor infomation which is pretty similar to a Python list. In locate(), which is the main feature of the app, there is a if statement checks whether an artwork is on view and whether its gallery information is available before changing floors. I can also recognize the while loop in loadGalleries(), which keeps loading gallery data until there are no more pages. Looking back to these codes, I can better understand how the app works and what is my AI actually working on.
