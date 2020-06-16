# card_catalog
## Project01 for PYTH-5-19

## Project Description
This is a card catalog of the sort that might have been seen on the only computer in a public library in 1991. Catalog items can be found via search and lent to borrowers, and each item type includes methods for "using" the item.

The user interface is based in a BASH terminal. To execute, type `python index.py` from within the project directory.

## Google Sheet
Include link to your google sheet here. Here is the URL [Suresh had used in class](https://docs.google.com/spreadsheets/d/1orcguDZd5ux2TfV5lf-E2z0xPQDT6FV69W4DIYdP2J0/edit?usp=sharing) 

#### MVP

Deliverables:

1) List a catalog of items
2) View and "use" individual items by catalog number
3) Search items by title or by author/artist
4) "Check out" items to borrowers and check them back in.
5) List borrowers along with items currently borrowed.

Approach:

| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Class logic | H | 1.5hr | 1.5hr | 1.5hr|
| Seed data  | H | .5hr | .5hr | .5hr|
| Program logic | H | 1.5hr | 2hr | 2hr|
| UI tweaks and BASH stylez  | M | .5hr| 1.5hr | 1.5hr |
| Error handling | H | .5hr | 1hr | 1hr|
| Total | H | 4.5hrs| 6.5hr | 6.5hr |

#### PostMVP

Deliverables:

1) Create new items
2) Create new borrowers
3) Show borrower history
4) Integrate with SQL database

Approach:

| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Logic for item create | H | .75hr | .5hr | -hr|
| Logic for borrower create | M | .75hr | .5hr | .5hr|
| Borrower history logic & display | L | 1hr | -hr | -hr|
| Refactor for SQL | H | 3hr | -hr | -hr|
| Total | H | 5.5hrs| 1hrs | .5hr |

## Additional Libraries

- datetime
- math
- random
- os

## Code Snippet

I had not previously used `filter()` or lambda functions in Python, so I'm pleased that I was able to find a simple solution for searching by title.  

```python
def search_by_title():
    input_title = input("Enter a word in the title and press Enter: ")
    result = list(filter(lambda item: input_title.lower() in item.title.lower(), catalog))
    print_list(result)
    view_item()
```

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Description | Complete
|Day 1| Priority Matrix / Timeline | Complete
|Day 3| Core Application | Complete
|Day 4| MVP & Bug Fixes | Complete
|Day 5| Final Touches | Semi-complete
|Day 6| Deploy to GitHub | Complete

## Issues and Resolutions

**ERROR**:  Project breaks on any input out of prescribed range

**RESOLUTION**: Added new logic to catch and handle user errors

## To execute program in shell

`python index.py`
