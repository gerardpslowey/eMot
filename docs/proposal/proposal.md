# School of Computing &mdash; Year 4 Project Proposal Form


## SECTION A

|                     |                   |
|---------------------|-------------------|
|Project Title:       | xxxxxx            |
|Student 1 Name:      | Gerard Slowey     |
|Student 1 ID:        | 17349433          |
|Student 2 Name:      | Michael Savage    |
|Student 2 ID:        | xxxxxx            |
|Project Supervisor:  | Jennifer Foster   |


## SECTION B

> Guidance: This document is expected to be approximately 3 pages in length, but it can exceed this page limit.
> It is also permissible to carry forward content from this proposal to your later documents (e.g. functional
> specification) as appropriate.
>
> Your proposal must include *at least* the following sections.


### Introduction

> Describe the general area covered by the project.

Our project covers the general areas of data extraction, natural language processing, sentiment analysis, machine learnin, cloud computing and server-client communication. 

The resulting project will use a combination of the aforementioned technologies to analyse the web browsing activity of a user to extract sentiment from the sites that they have visited.

### Outline

> Outline the proposed project.

Our project is a client-server based application that will use natural language processing with sentiment analysis and machine learning. The aim of the application will be to help prevent end users from overwhelming themselves with negative content that is being viewed online.

The application will run locally in the background on the users machine (windows or linux). By recording the sites visited by the user, we aim to gauge the sentiment of the material they are reading or focusing on. This will be carried out by scraping text from websites using the recorded URLs.

Based on the browsing habits of the user a material sentiment graphical bar will indicate to the user the sentiment of the material they have been focusing using colours. If the user focuses primarily on negative material the progress bar will fill up quicker and eventually the user will be prompted to take a break from reading online material. 


### Background

> Where did the ideas come from?

This concept stemmed from the recent increase in time being spent online, due to the Covid-19 pandemic. Activities such as working from home can lead to loneliness and social isolation for many people. Combined this with focused attention on negatively skewed Covid-19 news can lead to a very bleak perspective of the future.

With reduced opportunities to combat these problems due to restrictions, it can be difficult to ‘escape’ the doom and gloom associated which may lead to negative mental health.


### Achievements

> What functions will the project provide? Who will the users be?

There are several main functions that our project offers:
- A local application on the users machine responsible for:
  - Recording the links clicked by the user / access the users browser history with their consent.
  - Storing and manipulating these links in a database.
- A web link scraper / crawler provided with relevant links from the database.
- Natural language processing of the scraped data.
- Analyses and scoring of the data.
- Interfacing with and notifying the user notified of their reading sentiment via graphical representation.


- This project will allow a user to regulate their browsing of online articles and pages without getting overwhelemed by negative content. Because the project tracks the sentiment of the material being viewed the user will be able to balance the sentiment of the material they read. 

This project could arguably be used by any person browsing the web. Once the application is running on the local machine and an internet connection exists, the user can let the application do all the work.

### Justification

> Why/when/where/how will it be useful?

### Programming language(s)

> List the proposed language(s) to be used.

Python

### Programming tools / Tech stack

> Describe the compiler, database, web server, etc., and any other software tools you plan to use.

### Hardware

> Describe any non-standard hardware components which will be required.

### Learning Challenges

> List the main new things (technologies, languages, tools, etc) that you will have to learn.

### Breakdown of work

> Clearly identify who will undertake which parts of the project.
>
> It must be clear from the explanation of this breakdown of work both that each student is responsible for
> separate, clearly-defined tasks, and that those responsibilities substantially cover all of the work required
> for the project.

#### Student 1

> *Student 1 should complete this section.*

#### Student 2

> *Student 2 should complete this section.*

## Example

<!-- Example: Here's how you can include images in markdown documents...

Basically, just use HTML! 

<p align="center">
  <img src="./res/cat.png" width="300px">
</p>

-->