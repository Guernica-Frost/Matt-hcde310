# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
def save_result(artworks, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(len(artworks)):
            f.write(artworks.get("title"), artworks.get("artist_title"), artworks.get("date_display"))

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*
See below ##5

## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*
I predict each line of the txt file will be: Artworks, Artist, Date. And those data are relevant to what I've searched.
Such as: Lion (One of a Pair, South Pedestal), Edward Kemeys, 1893, Bronze with green patina
Nude with Cats, Pablo Picasso, 1901, Oil on cardboard, etc
Real: AttributeError: 'list' object has no attribute 'get'

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*
I thought f.write() function can deal with multiple parameters, so I have like f.write(artworks.get("title"), artworks.get("artist_title"), artworks.get("date_display")) this statement. But it turns out to be wrong. Thus, I used an f-statement to combine the 3 parameters into 1.

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*
I add new data that is medium displayed in the txt file. Because in part1 #2, I wrote I want to show the medium fields to my users.


##2 Chat with AI
Full conversation
Me:

I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log.

My attempt so far:

import requests
FIELDS = "id,title,artist_title,artist_display,date_display,medium_display"
url = "https://api.artic.edu/api/v1/artworks/search"
params = {"q" : term, "fields" : FIELDS}
response = requests.get(url, params=params)
if response.status_code != 200:
    print("Request failed:", response.status_code, response.reason)
Where I'm stuck: Terminal returns me Request Failed: 403 forbidden.

Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put # AI-written on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code.

Claude (translated): I'll follow your rules, starting with the 403 problem.

Claude:

I'm not going to write a function for this one. The 403 comes from the Part 2 request code, and Part 2 is Stage 2 (Tutor), so your helper-prompt rule for "anything other than this one function" applies: hints and questions only. Keep the Stage 3 prompt for save_results in Part 4.

What 403 means: the museum's server got your request and refused it. A 404 would mean "wrong address" and a 500 would mean "the server broke". A 403 means "I know what you want, but I won't give it to you." So the problem is probably not your URL or your q.

Questions to work through:

Paste the same URL with ?q=cat into your browser. Does it work there? If it does, the URL is fine, and the question becomes: what is different between your browser asking and your Python script asking?
Every request also sends headers, short notes about who is asking. A browser says something like "I'm Chrome." requests says "I'm python-requests" by default. Some servers block that default.
Look at the Art Institute API docs (api.artic.edu/docs). Search the page for "User-Agent". What header do they ask you to send, and what do they want you to put in it?
New thing: headers= is an optional argument to requests.get. It takes a dictionary of header names and values and sends them with the request, the same way params= sends a dictionary.

One more thing in your file: the params line in fetch.py has "fields": "Fields", but the code in your message has FIELDS. That isn't what causes the 403, but what is the difference between the two? What would the API get in each case?

I couldn't test the live API from here, so tell me what you find in the browser test (question 1) and we'll go from there.

Me: it runs well with the same url with ?q=cat, so how should I fix that

Claude:

Good test. The browser gets a 200 and your script gets a 403 for the same URL, so the URL is fine. What's different is who is asking, and that goes in the headers. Here's how to fix it in steps. You write the code:

Find the header name. The Art Institute docs (api.artic.edu/docs, search the page for "AIC-User-Agent") say what to send. The value is your app's name plus your contact email, something like hcde310-hw3 (you@uw.edu).
Make a dictionary. You already built params as a dictionary of name → value. Make a second dictionary the same way: the key is the header name from step 1 and the value is your app name and email.
Pass it in. requests.get already takes params=params. Add one more argument next to it, headers=, and give it your new dictionary.
Before you run it, predict: what status code will you get now? And if you misspelled the header name, would you still get a 403?

If it's still 403 after this, paste your new requests.get line here and we'll look at it together. Also remember the "Fields" vs FIELDS question from before. Once the 403 is gone, check whether all your fields actually show up.

Me: I try to add a header to the links. My header statement is: headers={"AIC-User-Agent": "hcde310-hw3 (my uw email)"}, is it the right format for putting headers into link?

Claude:

Yes, that dictionary is the right format: the header name is the key and your app name plus email is the value, both as strings. Two small notes:

The course is HCDE 310, and you wrote hcde301. The server won't care, but fix it so it's accurate.
Make sure your real UW email goes inside the quotes, not the words "my uw email".
One thing to check in your wording: headers don't go into the link (the URL). params gets added to the URL as ?q=cat&fields=..., but headers travel separately, alongside the request. So the dictionary on its own does nothing yet.

Where does it need to go so requests.get actually sends it? Look at how params gets from its variable into the call, then do the same for headers. Run it and tell me what status code you get.

Me: I can access now, thank you

Claude:

Nice work, you fixed that yourself. 🎉 Two things before you move on:

Check the "Fields" vs FIELDS line in your params. Do all the fields you picked in Part 1 actually show up in your output now?
A quick question for your notes: why do you think the museum wants to know who is calling its API?
When you get to save_results in Part 4, bring the Stage 3 prompt back and we'll do Try → Predict → Run → Explain → Log there.

Me:

I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log.

My attempt so far:

def save_result(artworks, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(len(artworks)):
            f.write(artworks.get("title"), artworks.get("artist_title"), artworks.get("date_display"))
Where I'm stuck: Terminal returns me

File "/Users/taurus2nd/Desktop/HCDE310/Matt-hcde310/hw3/fetch.py", line 46, in <module>
    save_results(artworks, "result.txt")
  File "/Users/taurus2nd/Desktop/HCDE310/Matt-hcde310/hw3/fetch.py", line 23, in save_results
    f.write(artworks.get("title"), artworks.get("artist_title"), artworks.get("date_display"))
AttributeError: 'list' object has no attribute 'get'
The function I need: save_result(artworks, "result.txt") takes artworks list and "result.txt" and returns a txt file that writes one line per artwork (title, artist, date).

Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put # AI-written on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code.

Claude:

Here's the function:

# AI-written
def save_results(artworks, filename):
    """Takes a list of artwork dictionaries and a filename, writes one line per artwork (title, artist, date) to that file, and returns nothing."""
    with open(filename, "w", encoding="utf-8") as f:
        for artwork in artworks:
            title = artwork.get("title") or "Untitled"
            artist = artwork.get("artist_title") or "Unknown artist"
            date = artwork.get("date_display") or "Unknown date"
            f.write(f"{title} - {artist} ({date})\n")
I named it save_results with an s, not save_result. Your call on line 46 and check.py both use that name.

Predict before you run it: say artworks holds these three works from sample_response.json:

Lion (One of a Pair, South Pedestal), Edward Kemeys, 1893
Nude with Cats, Pablo Picasso, 1901
Baroque Pearl Mounted as a Cat Holding a Mouse, artist is null, 17th century
If you call save_results(artworks, "result.txt"), what exactly will result.txt contain? Write the lines as you expect them, and put your prediction in ai_log.md before you run anything.