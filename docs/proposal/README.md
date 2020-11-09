# School of Computing &mdash; Year 4 Project Proposal Form


## SECTION A


|Project Title:       |       Emot        |
|---------------------|-------------------|
|Student 1 Name:      | Gerard Slowey     |
|Student 1 ID:        | 17349433          |
|Student 2 Name:      | Michael Savage    |
|Student 2 ID:        | 17313526          |
|Project Supervisor:  | Jennifer Foster   |


## SECTION B


### Introduction

- Our project covers the general areas of data extraction, natural language processing, sentiment analysis and machine learning. 

- The resulting project will use a combination of the aforementioned technologies to analyse the web browsing activity of a user to extract sentiment from the sites that they have visited.

### Outline

- Our project is a locally hosted application that will use natural language processing with sentiment analysis and machine learning. 

- The aim of the application will be to help prevent end users from overwhelming themselves with negative textual content that is being viewed online.

- The application will run in the background on the users machine (windows or linux). By recording the sites visited by the user, we aim to gauge the sentiment of the material they are reading or focusing on. 

- This will be carried out by scraping text from websites using the recorded URLs.

- Based on the browsing habits of the user a material sentiment graphical bar will indicate to the user the sentiment of the material they have been reading using colours. 

- If the user focuses primarily on negative material the progress bar will fill up quicker and eventually the user will be prompted to take a break from reading online material. 

### Background

- This concept stemmed from the recent increase in time being spent online, due to the Covid-19 pandemic. Activities such as working from home can lead to loneliness and social isolation for many people. 

- Combining this with focused attention on negatively skewed Covid-19 or political news can lead to a very bleak perspective of the future.

- With reduced opportunities to combat these problems due to government restrictions, it can be difficult to escape the daily doom and gloom which may in turn lead to negative mental health.

### Achievements

- There are several main functions that our project will offer: 

1. A local application on the users machine responsible for:
    - Recording the links clicked by the user / accessing the user's browser history with their consent.
    - Storing and manipulating these links in a database.

2. A web link scraper / crawler:
    - It will be provided with relevant links from the database.

3. A Natural language processor of the scraped data. 
    - It will analyse and score the data.

4. An interface to view, use and be notified of reading sentiment via graphical representation.


- This project could arguably be used by any person browsing the web. Once the application is running on the local machine and an internet connection exists, the user can let the application do all the work.
- This project will allow a user to regulate their browsing of online articles and pages. The project tracks the sentiment of the material being viewed and the user should be able to balance the sentiment of the material they read. 

### Justification


- The use of a system like this would be beneficial in changing a persons browsing habits. If the project can make the user more aware of their inclined focus on negativity, then they should be able to be proactive and avoid it.

- This will be useful for people every time they browse websites on their PCs. This project could be used as a constructive learning experience about ones browsing habits.

### Programming language(s)

- Python will be the main langauge being used, due to its diversity and applications in the following areas:
    - web scraping, 
    - sentiment analysis, 
    - graphical user interface design
    - and database management.

### Programming tools / Tech stack

Our project will consist of the following tools:
- Database - Due to privacy concerns browsing data will be stored locally on the users machine using a SQLite database. The SQLite database can be interfaced using the sqlite3 python library.

- Parsing - Scrapy is a Python scraping framework that will be used to access website URLs supplied from the URL's database.

- Machine Learning - scikit-learn is the Python machine learning library that we will use to help us analyse data. 

- Testing - For testing, Python’s testing library PyUnit will be used for testing. Additional testing datasets will be used for testing the sentiment analyses aspects of the project also.

- Interface - Tkinter will be used to design a GUI for the program, through which the user will be presented with graphical representations of their browsing sentiment.

### Hardware

- The software for this project will be runable on any standard Linux or Windows machine.

### Learning Challenges

- Sentiment Analysis - We need to learn how to use natural language processing in Python. We want to build our own analyser and this will require research.

- SQLite - A refresh of our SQL knowledge will be required to be able to construct queries to the database.

- Parsing - We need to understand how to extract relevant information from the user's browser history. This will involve working with HTMl data. We will need to strip away the HTML tags and code to extract the useful text.

- GUI - We need to figure out how to create a good GUI in Python using Tkinter GUI. We have both used the Python FLASK API before so it should be a progression on from that.

- Machine Learning - This will be built with scikit-learn and we need to understand our datasets and how to incorporate them. We had a brief introduction to numpy and neural networks last year.

### Breakdown of work

#### Michael

Both team members will divide the work on:
- Machine Learning for sentiment.
- Testing our code, program perfromance and accuracy.

Michael will primarily in charge of:
- Text scraping using Scrapy.
- Using Tkinter GUI to run the program.
- Setting up SQLite.

#### Gerard

- Natural Language processing.
- Getting access to the browser history for parsing.
- Sending responses to user and updating visual data.


| Student                       |Michael            | Gerard            |
|-------------------------------|-------------------|-------------------|
| Testing                       |         X         |         X         |
| Machine Learning              |         X         |         X         |
| Natural Language Processing   |                   |         X         |
| GUI                           |         X         |                   |
| Scraping URL                  |         X         |                   |
| Parsing URL                   |                   |         X         |
| Presenting Data               |                   |         X         |
| Database                      |         X         |                   |
