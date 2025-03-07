# Glint Solar test assignment
## Install
1. Clone the repo
2. Make sure you have python installed (v3 preferably)
3. Run following commands from inside the project root:
    - `python -m venv .venv`
    - `source .venv/bin/activate`
    - `pip install -r requirements.txt`
    - `fastapi dev main.py`
4. Open `index.html` file in browser
5. Click on any point on the map

## Questions
> 3. Imagine instead of providing the answer for the max wave for a single day, we want to
answer what is the max wave since 1950 (since the max over the last 70+ years will be a
better indicator of the worst they should expect than just a single day of data). Describe
in brief terms how you would go about solving this problem. What are your main points of
concern to make this possible.

Main point of concern would be a response time for request. Using a database would allow to operate such large dataset (~80 years of data) quickly and efficiently. Indexing columns is necessary to optimize a query which would find the maximum wave height for given coordinates. In our case I'd put indexes on longitude and latitude columns and use `max()` SQL operator to find a max weight height value.

## Additional thoughts
- Please don't judge the code too harshly. My Python knowledge is limited to a university "Databases" course project I took 10 years ago :)