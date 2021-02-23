# Machine Learning and the Hall of Fame
## Introduction

The National Baseball Hall of Fame inducted its first eligible members in 1936.  Soon after, in 1939, the Baseball Hall of Fame Museum was opened in Cooperstown, NY.  Since its establishment, each year members of the Baseball Writer's Association of America (BBWAA) vote on eligible candidates to be inducted into the Baseball Hall of Fame.  Major League Baseball players are considered eligible candidates if the baseball player:

* Was an active MLB player at least 15 years prior to the year of the election.
* Has been retired for at least 5 years prior to the election.
* Has played in a minimum of 10 seasons.
* Cannot be on the Baseball Hall of Fame ineligible list.  

Once a candidate is deemed eligible, multiple criteria are taken into consideration when voting occurs, such as the player's record/statistics, ability, integrity, and contribution to a team.  Members of the BBWAA cast no more than 10 votes on each years ballot for the candidates of their choosing.  Any candidate that receives votes on at least 75% of the ballots will be inducted to the Hall of Fame.

**Team members:** Cale Green, Camille Goodwin, Claire Davis, Matt Martin, Silas Cobb, Trey Wehrmeyer

## Can Machine Learning be used to identify MLB Hall of Famers?

Taking into consideration the process and requirements of being inducted into the Baseball Hall of Fame, a machine learning model will be developed and used to identify past Hall of Famers and predict future inductees.  In addition, this model will help recognize historically underrated players and examine the statistically-worthy players who have not yet been inducted to the Hall of Fame.  Ideally, the machine learning model will be able to be applied to future datasets and predict Hall of Fame inductees with an above average level of accuracy.

# Table of Contents
- [Machine Learning and the Hall of Fame](#machine-learning-and-the-hall-of-fame)
  - [Introduction](#introduction)
  - [Can Machine Learning be used to identify MLB Hall of Famers?](#can-machine-learning-be-used-to-identify-mlb-hall-of-famers)
- [Table of Contents](#table-of-contents)
  - [Communication](#communication)
  - [Technologies](#technologies)
  - [Resources](#resources)
  - [Data Exploration](#data-exploration)
  - [Extract, Transform, Load](#extract-transform-load)
  - [Database](#database)
  - [Machine Learning Model](#machine-learning-model)
  - [Visualizations](#visualizations)
  - [Deployment](#deployment)

## Communication

The below methods of communication have been agreed upon by all team members and will be utilized daily and weekly to successfully complete the project:

* GitHub will house the project's repository where team members will be able to push completed work to feature branches, which will then be merged to the main accordingly.
* Zoom virtual meetings as needed outside of devoted Tuesday and Thursday evenings to further supplement collaboration and progress.
* Slack messaging to post and share a running thread of resources, ideas, and updates visible to all team members.
*  A Trello board will be utilized to better manage incomplete, in progress, and completed tasks for the project by team members.  

## Technologies

The following various technologies will be used throughout the completion of this project:

* Python and Pandas for data exploration and ETL
* PostgreSQL for a database
* Random Forest Classifier machine learning model
* Matplotlib for visualization of findings
* Heroku, Flask, HTML, and JavaScript for dashboard creation and deployment

## Resources

[Baseball-Reference.com: MLB Stats, Scores, History, and Records](https://www.baseball-reference.com/ "Baseball-Reference.com")


[Baseball Database](http://www.seanlahman.com/baseball-archive/statistics/ "Sean Lahman's Baseball Database")

## Data Exploration

## Extract, Transform, Load
Pitching ETL:

- Within the Career_Pitching_df our first focus was to read in and merge our pitching and Hall of Fame CSV’s.  We cleaned up the data by removing players who would not qualify for the Hall of Fame based on their time played in the MLB. This allowed us to then focus on the stats that are important in determining what a Hall of Fame player should look like. Not every statistic we wanted was provided so we had to add several columns to our data frame.   Some of the stats we wanted to make sure we added were pitchers' Inning Pitched (IP), Win Percentage, Strikeout to Walk Ratio, and Walks Plus Hits Per Inning Pitched (WHIP).
- We did run into an issue early on when creating the Career_Pitching_df.  We found that the CSV file did not have the correct pitcher ERA because the IPOuts column was not in its final form.  We had to add an IP column by dividing the IPOuts by three.
## Database

## Machine Learning Model

## Visualizations

## Deployment
For User-Facing purposes - a combination of 
- HTML 
- CSS 
- Bootstrap 
- JS 
- Python
- Flask 
have been utilized to build a dynamic webpage that with current functionality to 
- Scrape the top article from the Basball Hall of Fame's website
- As well as pictures from the Hall's image gallery
- Create a dropdown list of Hall of Fame candidates throughout the history of baseball.
- Additional functionality to be added shortly!

### Heroku 
Heroku is a cloud-based service that has the functionality to connect to Github, which creates automatic deployment of our project.  
Continuous code can be committed to the repository and then deployed within the Heroku platform by initially setting up the following files:
* h_app: is the app folder created to contain the flask app and supporting templates
	* __init__.py: the file that creates the flask app and additional routes
	* templates: the folder created within the app folder to organize html files
		* base.html: creates the initial structure for our webpage
		* index.html: an extension from our base.html and contains the main content
* Procfile: this is file specifically used for Heroku to create the webserver and initialize the starting point
* requirements.txt: this text file shows all the packages being used 
* wsgi.py: this file imports our flask app

