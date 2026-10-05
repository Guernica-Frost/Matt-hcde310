# AI log

## HW0: Class 1, build an app with AI

Paste every prompt you sent, in order, with the AI's replies. A share link to the chat is fine too, but paste the prompts here either way. Your thinking about it goes in `day1.md`.

**Share link (optional):**

### Prompt 1

```
Build a single-page interactive web app. It calls the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. Keep it under ~150 lines. It's for first-time visitors to the Art Institute of Chicago who want to find where a specific artwork is located in the museum before their visit. My sketch is attached; follow it. Explain how the code works in plain language, section by section.
```

**AI's reply:**

No sketch was attached and the project folder is empty, so I'm building the app with a standard layout for now — I'll adjust it once I see your sketch.

Created index.html, ran a command, used 3 tools
The image URLs are correct and load from the command line. The preview shows the page from a data: URL, which may be what's blocking them, so I'll try serving it from a real local server.

static
Browser tab closed
Created launch.json, ran a command, used 6 tools (2 failed)
I built the app in index.html. It's 141 lines. Your sketch didn't come through (the message had no attachment and the folder was empty), so I used a common layout: a header, then a search bar with filters, then a grid of result cards. Send the sketch and I'll change the layout to match it.

Testing: Searching "Nighthawks" returned real results with the right locations, such as Nighthawks → Gallery 262 and American Gothic → Gallery 263. The images didn't show up in my test browser. That browser blocks the museum's image server, and the requests never went out. I checked one image address from the command line and got a valid JPEG back, so they should load in Chrome or Safari. I couldn't confirm that myself.

To try it, open the file in your own browser:

open /Users/taurus2nd/Desktop/HCDE310/index.html
How the code works, section by section
1. The <head> and styles. This part sets the page title and how everything looks. The colors are defined once at the top (--accent is the museum's red) and reused throughout. Results sit in a grid that fits as many cards per row as the screen allows, so it works on a phone too. Each card has a colored "where" box: green when the artwork is on view, grey when it isn't. That box is the most important thing for a visitor.

2. The header. A banner that tells a first-time visitor what the page is for: find which gallery an artwork is in.

3. The search form. Three controls:

A text box for an artwork title or artist name.
A department dropdown. I took these names from the API's list of departments that have works on view.
An "On view only" checkbox, checked by default. Before a visit, people mostly want works they can actually go and see.
4. buildUrl(). This turns the form into a web address for the API.

It always sends your search text (q).
It asks only for the details the page needs (fields), which keeps responses small and fast.
It limits results to 24.
Each active filter is added as a "must match" rule. For example, "must be on view" plus "must be in the Arts of the Americas department".
5. renderCard(). This takes one artwork from the API and makes a card for it.

Image: the API gives each artwork an image_id. You combine it with the museum's image server address to get a picture. Some works have no image, so those get a placeholder.
Location: if the work is on view, the card shows its gallery (like "📍 Gallery 262"). Otherwise it says "Not currently on view".
Link: each card links to the artwork's page on artic.edu.
6. escapeHtml(). A small safety step. Some titles contain characters like < or &. This keeps them from breaking the page or being read as code.

7. search(). This runs every search:

It reads the form and builds the URL.
It shows "Searching…" and clears the old results.
It fetches the data and waits for the reply (await).
It then shows one of three outcomes: a "no results" message, the result cards with a count, or a friendly error if the museum's server can't be reached.
8. Event listeners (the last few lines). Pressing Enter or clicking Search runs a search. Changing the department or the checkbox runs it again right away, so filters apply instantly.

I also added .claude/launch.json so I could run a local preview server. It isn't part of the app, and you can delete it.

open /Users/taurus2nd/Desktop/HCDE310/index.html
[No output was captured. The command ran in the terminal pane (tab 0); if it should have printed something, use read_terminal with tab_id "0" to check.]
That should have opened the page in your default browser. Try searching "Nighthawks" to check the two things I couldn't confirm myself:

Images: they should appear on each card. If they're still blank, tell me which browser you're using and I'll look into it.
Location badge: Nighthawks should show 📍 Gallery 262 in green.
Your sketch still hasn't come through. When you send it, I'll change the layout to match.

### Prompt 2

```
Build a single-page interactive web app. It calls the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. Keep it under ~150 lines. It's for first-time visitors to the Art Institute of Chicago who want to find where an artwork is located in the museum before their visit. My sketch is attached; follow it. Explain how the code works in plain language, section by section.

Details from our sketch:
- Top left: a simple logo. Top right: a search bar with an info (i) icon next to it.
- Left side: a vertical, scrollable floor index (3F, 2F, 1F, -1F/Lower Level). Clicking a floor shows that floor in the center.
- Center: a floor plan of the selected floor, with the artworks on that floor shown as clickable items. Build the floor plan from the API's /api/v1/galleries endpoint (each gallery has floor, latitude, and longitude) instead of using an image of the official map.
- Most important moment: when the user clicks an artwork in the search results, the center automatically jumps to the floor where that artwork is displayed (using its gallery_id) and highlights it. If is_on_view is false, show "Not currently on view."
```

**AI's reply:**

The fix works for normal browsers—the AIC server only blocks the localhost Referer (now fixed) and the preview pane's uneditable user agent, while a regular Chrome UA with no referrer returns 200. I'll now trim the file from 162 lines closer to the ~150 target.

I built the app as floor-finder.html, at 152 lines. I didn't touch your existing index.html, because it's an earlier list-style version of the project.

What I tested in the preview pane:

Floor plans: clicking 3F, 2F, 1F and -1F redraws the center with that floor's galleries and its most popular works.
Jump to floor: searching "Nighthawks" and clicking the result switched to 2F, outlined Gallery 262 in red, and showed a pulsing ring with a "★ Nighthawks" label. "Water Lilies" jumped to Gallery 243 in the same way.
Not on view: clicking Arrival of the Normandy Train showed "Not currently on view."

Images: I couldn't see them load in the preview pane, so check them yourself. The museum's image server blocks the pane's own browser. It also blocks image requests that say they come from localhost, so I added a line in the page's header that stops the browser from sending that information. With an ordinary Chrome browser and that setting, the images load fine when I request them directly. Open the file in Chrome or Safari to confirm the pictures appear.

open /Users/taurus2nd/Desktop/HCDE310/floor-finder.html
How the code works, section by section

1. Page layout (HTML)
The page follows your sketch:

Header: the logo box is on the left. On the right are the i button and the search bar. Clicking i opens a short "how to use" box.
Main area: three columns.
Left: the floor buttons. This column scrolls if it gets too tall.
Center: a status line, the floor plan, and a details card.
Right: the search results list.

2. Styling (CSS)
This controls colors, spacing and the three-column grid. A few parts worth knowing:

The floor plan is tilted back slightly (rotateX(24deg)) to look like the slanted floor in your sketch.
The .hot styles are the "you found it" look: a red room outline and a pulsing ring around the artwork.
On narrow screens the results list moves below the map.

3. Setup

These are fixed values: the API address, the image server address, and the four floors. The museum's data calls the lower level LL, and the app shows it as "-1F".
FIELDS lists the few facts the app asks for about each artwork: title, artist, image, gallery, and whether it's on view.
esc() cleans up artwork titles before they go on the page, so characters like & or < don't break it.

4. Talking to the API

searchArt() sends every artwork request to /artworks/search. Your search words and the floor filter both go through this one function.
loadGalleries() runs once when the page opens. It reads every page of /galleries and keeps the ones that have a floor and a map position. There are about 170.
It then finds the outer edges of all galleries combined, so every floor is drawn at the same scale.
xy() turns a gallery's latitude and longitude into x/y positions on the drawing. North is up and east is right.

5. Drawing a floor

showFloor() is what clicking a floor button does. It highlights the button and picks out that floor's galleries.
It then makes a filtered API call: "the 30 most popular works that are on view in these galleries."
A counter (drawId) handles fast clicking. If you click floors quickly, only the last answer is drawn.
drawPlan() draws each gallery as a rounded square with its gallery number underneath.
Each artwork is a small round picture placed on its gallery. Works in the same room are spread out around it so they don't stack.
The highlighted work is drawn last and larger, so it sits on top, with a "★ title" label above it.

6. The jump-to-floor moment

showDetail() fills the card under the map with the picture, title, artist and date, plus where to find it:
"📍 Gallery 243 · 2F" if it's on view,
"Not currently on view." if is_on_view is false,
a note saying it's on view but not on this map, if its gallery has no map position.
locate() is what clicking an artwork does, in the results or on the map.
It shows the details, then uses the artwork's gallery_id to find its gallery and floor.
It then calls showFloor() for that floor with the artwork marked to be highlighted. If the artwork isn't among that floor's top 30, it's added so it always appears.

7. Hooking up clicks

One listener on each area handles its clicks: floor buttons, map items, results, the i button, and the search form.
Submitting the search asks for 20 matches and lists each one with a small picture and a quick hint, such as "2F · Gallery 262" or "Not currently on view."
The last line loads the galleries and opens on 1F.

Limitation: the API only gives a center point for each gallery, not its walls. The plan shows where rooms are relative to each other, not their real shapes. The help text tells visitors this.

The page should now be open in your default browser, but I can't see that window. Here's what to check:

Pictures: thumbnails should appear in the search results and as round pictures on the floor plan. If they're gray boxes, tell me which browser you're using.
Map: opening it straight from the file (file://) should work the same as through the preview server. The museum's data allows requests from any page, including a local file.
Key moment: search "Nighthawks", click the first result, and the map should jump to 2F with Gallery 262 outlined in red.

If anything looks off, a screenshot is the quickest way for me to fix it.

(Copy the block above for more prompts.)
