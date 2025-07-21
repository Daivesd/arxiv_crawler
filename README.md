# arxiv_crawler

Goal: create & update an arxiv database of relevant papers (based on keywords, authors). If possible the database should be viewable for example via a browser, and it should be possible to notify users (for example via a weekly email) of new entries


Parts that go into this:
- Scraping the data from arxiv 
  - Arxiv api
  - Has keywords/authors and such as input
  - Should/could run on a certain schedule
  
- Parsing the data into a database
  - Extract the relevant fields
  - Structure into a database
  - Uses feedparser for parsing, pandas for database
  
- Making the database accessibele 
  - As html table from pandas database

- Notifying via email
  - On a schedule, check for new entries in some time range
  - Email userlist the new entries
