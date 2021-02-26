---
marp: true
theme: base
#class: invert
---
# Machine Learning and the Hall of Fame
Cale Green, Camille Goodwin, Claire Davis, Matt Martin, Silas Cobb, Trey Wehrmeyer

---
## Overview
- Idea
- Resources
- ETL
- Database
- Machine Learning Model
- Web App
- Live Demo

---
# Idea 
Can machine learning be used to predict future baseball Hall of Famers?

Taking into consideration the process and requirements of being inducted into the Baseball Hall of Fame, a machine learning model will be developed and used to identify past Hall of Famers and predict future inductees. In addition, this model will help recognize historically underrated players and examine the statistically-worthy players who have not yet been inducted to the Hall of Fame. Ideally, the machine learning model will be able to be applied to future datasets and predict Hall of Fame inductees with an above average level of accuracy.

---
# Resources


*[Sean Lahman's Baseball Databse](http://www.seanlahman.com/baseball-archive/statistics/)*

*[Baseball Reference](https://www.baseball-reference.com/)*

*[Baseball Hall](https://baseballhall.org/)*

Tables Used:
- Pitching.csv
- Batting.csv
- HallOfFame.csv


---
# ETL
Batting ETL:


Pitching ETL:

---
# Database
Connected to postgres from ETL IPYNB. Pulled tables from postgres database to machine learning notebooks
---
# Machine Learning Model
Random Forest Classifier and Logistric Regression

---
# Web App

---
# Live Demo

---
# Technologies Used

- Python and Pandas for data exploration and ETL
- PostgreSQL for a database
- Random Forest Classifier machine learning model
- Matplotlib for visualization of findings
- Heroku, Flask, HTML, and JavaScript for dashboard creation and deployment