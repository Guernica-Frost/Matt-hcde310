# In-class 6 notes

## What happens with a wrong key? What status code?

I tested the script with an invalid API key. NASA returned status code 403
(Forbidden). The script printed the status code and an error message, then
stopped without trying to read any photo data.

## Where does your key live, and why isn't it in earth.py?

My API key lives in the local in-class-6/.env file as NASA_API_KEY.
It is not written directly in earth.py because that file will be committed
and pushed, which would expose the key. 
And I added .env file into .gitignore. So git command won't push that to github.

## Stuck? Where?

No blockers. With the configured key, the request returned status code 200
and the script printed the first photo's caption and date.
