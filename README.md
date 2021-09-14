# SFIAProject1

A Flask Application with CRUD Functionality

#Table of contents
---------------------

1 - Project Overview
2 - Project Tracking
3 - Risk Assessment
4 - Architecture
    4.1 - ERD
    4.2 - DB
    4.3 - CI Pipeline
5 - Testing
6 - The App
7 - Reflections
8 - Conclusion
9 - Refs
10 - Acknowledgements

----------------------

#1 - Project Overview
--------------------
The project assigned was to create a Flask application using Python, Flask, various modules within flask and then use of other technologies like Jenkins for Builds and Selenium for testing. The application will be able to utilise CRUD functionality within a database (CREATE, READ, UPDATE, DELETE) in order to manipulate or read data and will have an interface in orer to aid that.

To begin, I created the various planning documentation such as an ERD, a KANBAN board (using TRELLO) to enable tracking of my progress and potential sprints and a risk assessment.

I will also be utilising various technologies for continuous integration such as GIT and Jenkins for version control and webhook integration for the testing of my application builds.

The basic idea for the app is a blog posting board with basic login/signup functions, this will enable me to hit all of the checkpoints for CRUD functionality.
--------------------

#2 - Project Tracking
---------------------

Using KANBAN boards to track my progress from the earlier stages, it became clear as I slowly progressed than I had in fact bitten off more than I could chew for a basic CRUD app with my previous attempt at a project, so in order to ensure a decent attempt, I started from scratch and endeavoured to K.I.S.S. as my previous assessments had taught me. 

starting on wednesday 8th september, I began a new Trello board to replace my overcomplicated first attempt, and below is said board.


-------------------------

#3 - Risk Assessment

Find below the risk assesment for the application based upon likelihood of problem and mitigation strategy


---------------------------

#4 - Architecture
---------------------------

in the following sections I will be showing the design and architecture phases of the app

--------------------------
#4.1 - ERD
Please find below the ERD for the application that was designed before creation of the program

--------------------------------

#4.2 - DB

found below is the code used to create the database, found within the models.py file
-------------------------------

#4.3 - CI Pipeline
--------------------------------

For utilisation of the CI pipeline, I used multiple programs and tools such as Trello, Python, Flask, git and Jenkins for builds.

utilising the python programming language and the flask microframework, the app was esigned and created, utilising majority python, and then also utilising the HTML language to design and create the application itself, I also wanted to showcase my prior knowledge for this project by standardising all of the pages within the application using CSS to add style and flair.

this code was stored locally and remotely utilising the version control software git, this enabled me to build the application piece by piece while retaining the ability to rollback to previous versions in case a new push broke the application or caused any bugs not present in previous versions.





-----------------------------------------
#5 - Testing

Testing was one of the key components for this project, and while I didn't manage to accomplish too much on this front due to finding myself in hospital towards the latter end of the project, I started writing tests for the CRUD functionality which can be found below. 



#6 - The application
------------------------------------

within my application I tried to showcase my ability to create a very nice looking page for my web app, utilising the CSS portion of web design, which allowed me to supplement the basic functionality with a more impressive front end.

the first page is the home page, which has multiple buttons or "on click events" that lead to other pages and functions within the application.

the application features a login system with form input validation, and the ability to check the database for a duplicate email or username, preventing duplicates within the database.

you can logout of the application using the button named so and can login as many times as you like, the account page shows the logged in accounts username, while the home page showcases the posts made on app creation.

----------------------------------------

#7 - Areas of improvement

If I was to complete this project again, I would better utilise my time by trying to keep the scope of my project small, to prevent complete purge of the entire project and starting from scratch so close to the end of the deadline. 

it's also unfortuamte that I ended up in hospital, however this cannot be helped and also shouldn't have gotten in the way, but it did due to bad time management.

------------------------------------------