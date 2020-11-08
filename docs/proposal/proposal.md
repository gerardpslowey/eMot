# School of Computing &mdash; Year 4 Project Proposal Form


## SECTION A
---

|Project Title:       | Sentiment Insight |
|---------------------|-------------------|
|Student 1 Name:      | Gerard Slowey     |
|Student 1 ID:        | 17349433          |
|Student 2 Name:      | Michael Savage    |
|Student 2 ID:        | 17313526          |
|Project Supervisor:  | Jennifer Foster   |
|                     |                   |

## SECTION B
---

### Introduction

> Describe the general area covered by the project.

```
Our project covers the general areas of data extraction, natural language processing, sentiment analysis, machine learning, cloud computing and server-client communication. 

The resulting project will use a combination of the aforementioned technologies to analyse the web browsing activity of a user to extract sentiment from the sites that they have visited.
```
### Outline

> Outline the proposed project.

```
Our project is a client-server based application that will use natural language processing with sentiment analysis and machine learning. The aim of the application will be to help prevent end users from overwhelming themselves with negative content that is being viewed online.

The application will run locally in the background on the users machine (windows or linux). By recording the sites visited by the user, we aim to gauge the sentiment of the material they are reading or focusing on. This will be carried out by scraping text from websites using the recorded URLs.

Based on the browsing habits of the user a material sentiment graphical bar will indicate to the user the sentiment of the material they have been focusing using colours. If the user focuses primarily on negative material the progress bar will fill up quicker and eventually the user will be prompted to take a break from reading online material. 
```

### Background

> Where did the ideas come from?

```
This concept stemmed from the recent increase in time being spent online, due to the Covid-19 pandemic. Activities such as working from home can lead to loneliness and social isolation for many people. Combined this with focused attention on negatively skewed Covid-19 news can lead to a very bleak perspective of the future.

With reduced opportunities to combat these problems due to restrictions, it can be difficult to ‘escape’ the doom and gloom associated which may lead to negative mental health.
```

### Achievements

> What functions will the project provide? Who will the users be?

```
There are several main functions that our project offers.

1. A local application on the users machine responsible for:
  - Recording the links clicked by the user / accessing the user's browser history with their consent.
  - Storing and manipulating these links in a database.

2. A web link scraper / crawler.
- It will be provided with relevant links from the database.

3. A Natural language processor of the scraped data. It will:
- Analyse and score the data.

4. An interface to view, use and be notified of reading sentiment via graphical representation.
```

```
- This project will allow a user to regulate their browsing of online articles and pages without getting overwhelmed by negative content. The project tracks the sentiment of the material being viewed and the user should be able to balance the sentiment of the material they read. 

This project could arguably be used by any person browsing the web. Once the application is running on the local machine and an internet connection exists, the user can let the application do all the work.
```

### Justification

> Why/when/where/how will it be useful?

```
- The use of this project is built into the achievement of it. If the project can make the user more aware of negativity, then they should be able to be proactive and avoid it as they learn about their habits.

- This will be useful for people for every time they browse websites on their PCs. It should therefore be justified as a constructive learning experience about themselves.
```

### Programming language(s)

> List the proposed language(s) to be used.

```
Python - scraping; sentiment analysis, GUI
C - SQLite
```

### Programming tools / Tech stack

> Describe the compiler, database, web server, etc., and any other software tools you plan to use.

```
Database - Due to privacy concerns browsing data will be stored locally on the users machine using a SQLite database. The SQLite database can be interfaced using the sqlite3 python library.

Parsing - Scrapy is a Python scraping framework that will be able to access website URLs.

Machine Learning - scikit-learn is a Python machine learning API that will help us analyse data. 

Testing - In terms of tests, Python’s testing library PyUnit will be used for testing.

Interface - Tkinter will be how the user views the application.
```

### Hardware

> Describe any non-standard hardware components which will be required.

```
This project will be entirely software based.
```

### Learning Challenges

> List the main new things (technologies, languages, tools, etc) that you will have to learn.

```
Sentiment Analysis - We need to learn how to use natural language processing in Python. We want to build our own analyser and this will need good research.

SQLite - We have used Firebase for a NOsql approach so we need to learn how to use this database and the language with it.

Parsing - We need to understand how to extract relevant information from the user's browser history. This will involve working with JSON formatting and manipulating it.

GUI - We need to figure out how to create a good GUI in Python using Tkinter GUI. We have both used the Python FLASK API before so it should be a progression on from that.

Machine Learning - This will be built with scikit-learn and we need to understand our datasets and how to incorporate them. We had a brief introduction to numpy and neural networks last year.
```

### Breakdown of work

> Clearly identify who will undertake which parts of the project.
>
> It must be clear from the explanation of this breakdown of work both that each student is responsible for
> separate, clearly-defined tasks, and that those responsibilities substantially cover all of the work required
> for the project.

#### Michael

```
- Text Scraping using Scrapy
- Looking at Machine Learning will be split evenly
- Using Tkinter GUI to run the program
- Setting up SQLite
- Testing will also be split evenly.
```

#### Gerard

```
- Natural Language processing
- Machine learning
- Getting access to the browser history for parsing
- Sending responses to user and updating visual data.
- Testing
```