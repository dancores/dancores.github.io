# dancores
Dynamic website providing information on Danish Life Science Core Facilities.

## Documentation

* `publish.py` retrieves the Core facilities information from [https://docs.google.com/spreadsheets/d/1DqCJy4qOGNR4UD-PLHOQwyByDBlHdS4NLL-_jd4JS9U]() using pandas and then compiles `build/index.html` using jinja2.  
* A GH action (under `.github/workflows`) builds the website every 10 min and deploys it to the `gh-pages` branch (which then is hosted as a static website by GitHub).
