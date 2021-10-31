# Scraping Data
### Get public data and save in database

### This is project use
- Python

### How to run a project
1 - Clone the repository
2 - Install beautifulsoup4

---
    pip3 install beautifulsoup4
---

**IMPORTANT**
This project send data on Transfermarkt to database of Soccer API.

### How to work the project

1 - The script _index.py_ get data on transfermarkt and generate a CVS files for each season a player in repository ./csvFiles

2 - The script _updateDB.py_ get all CSV files on ./csvFiles and send all data to Soccer API, after all detele all CSV files on ./csvFiles
