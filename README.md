<p align="center"> 
  <img src="Images/nb_logo.png">
</p>
 <p align="center"> Machine Learning and the Baseball Hall of Fame </p>

## Introduction

The National Baseball Hall of Fame inducted its first eligible members in 1936.  Soon after, in 1939, the Baseball Hall of Fame Museum was opened in Cooperstown, NY.  Since its establishment, each year members of the Baseball Writer's Association of America (BBWAA) vote on eligible candidates to be inducted into the Baseball Hall of Fame.  Major League Baseball players are considered eligible candidates if the baseball player:

* Was an active MLB player at least 15 years prior to the year of the election.
* Has been retired for at least 5 years prior to the election.
* Has played in a minimum of 10 seasons.
* Cannot be on the Baseball Hall of Fame ineligible list.  

Once a candidate is deemed eligible, multiple criteria are taken into consideration when voting occurs, such as the player's record/statistics, ability, integrity, and contribution to a team.  Members of the BBWAA cast no more than 10 votes on each years ballot for the candidates of their choosing.  Any candidate that receives votes on at least 75% of the ballots will be inducted to the Hall of Fame.

:baseball: **Team members:** Cale Green, Camille Goodwin, Claire Davis, Matt Martin, Silas Cobb, Trey Wehrmeyer :baseball:

## Can Machine Learning be used to identify MLB Hall of Famers?

Taking into consideration the process and requirements of being inducted into the Baseball Hall of Fame, a machine learning model will be developed and used to identify past Hall of Famers and predict future inductees.  In addition, this model will help recognize historically underrated players and examine the statistically-worthy players who have not yet been inducted to the Hall of Fame.  Ideally, the machine learning model will be able to be applied to future datasets and predict Hall of Fame inductees with an above average level of accuracy.

# Table of Contents
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
    - [Heroku](#heroku)
  - [Credits](#credits)

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


[Sean Lahman's Baseball Database](http://www.seanlahman.com/baseball-archive/statistics/ "Sean Lahman's Baseball Database")


[Baseball Hall](https://baseballhall.org/)


[Fangraphs](https://www.fangraphs.com/)


## Data Exploration

## Extract, Transform, Load

Batting ETL:

- When creating our Career_Batting_df we started by reading in the Batting.csv and HallOfFame.csv from Sean Lahman's Baseball Database. 
The HallOfFame dataframe was then filtered to only include members inducted as players, omitting executives/pioneers, managers, and umpires.
In order to clean up the data, we took out columns that had high null values (CS, IBB, GIDP). Individual player seasons were then grouped together
to create a dataframe of career batting statistics, and then the 'yearID' and 'stint' columns were dropped from the dataframe, and new columns were created to add several key statistics (Batting Average(AVG), On Base Percentage(OBP), and Slugging Percentage(SLG)). Further remaining null values
in the dataframe were then replaced with zeroes. At this point the career batting dataframe and Hall of Fame dataframe were merged together
to create a new dataframe of career statistics with Hall of Fame status included. This dataframe was then filtered to omit players who had never had an official MLB at-bat. Finally, 
an additional level of filtering was added to omit pitchers inducted to the Hall of Fame from the batting database, as their inclusion would otherwise
skew the results of the model (players with under 3000 career at-bats who had been inducted to the Hall of Fame were omitted, which removed 71 entries from the dataframe).
At this point, our training dataframe was complete, containing 17,522 of the roughly 20,000 players to have appeared in Major League Baseball history, and all of
the position players to be elected to the Hall of Fame. 
- One of the issues we ran into on the Career_Batting_df was making our filter too narrow. We started by creating a filter of 2,000 at-bats(Ab) or higher and this ended up dropping our eligible player much lower than we wanted. 
We ended up filtering out any player who did not have an AB in the MLB since that helped eliminate pitchers and players with limited or no batting stats. One final
issue that arose in the process of creating our training dataframe was how to handle pitchers in the batting dataframe. National League pitchers and any pitcher to play before
the advent of the Designated Hitter rule accumulated fairly large amounts of career at-bats, with near universally poor performance. Because any of the pitchers would show up
as a Hall of Fame inductee in our dataframe, we decided to omit them from it, due to the likelihood that it would skew the machine learning model's performance. 

Pitching ETL:

- Within the Career_Pitching_df our first focus was similar to before where we read in and merged our pitching and Hall of Fame CSV’s.  We cleaned up the data by removing players who would not qualify for the Hall of Fame based on their time played in the MLB. This allowed us to then focus on the stats that are important in determining what a Hall of Fame player should look like. Not every statistic we wanted was provided so we had to add several columns to our data frame.   Some of the stats we wanted to make sure we added were pitchers' Inning Pitched (IP), Win Percentage, Strikeout to Walk Ratio, and Walks Plus Hits Per Inning Pitched (WHIP).
- We did run into an issue early on when creating the Career_Pitching_df.  We found that the CSV file did not have the correct pitcher ERA because the IPOuts column was not in its final form.  We had to add an IP column by dividing the IPOuts by three.

## Database

Once ETL was finalized we worked on putting the four data frames created (career_batter_df, hall_batter_df, career_pitching_df, and hall_pitching_df) into a local host PostgreSQL database. We were able to create a connection by adding code into the Career_Batters and Career_Pitching IPYNB files. Steps taken to create this connection were to import create_engine from sqlalchemy, import the databse password from a config file, create a connection string and database engine, then to import each table. 

Once our tables were created in Postgres, the next step was to pull the tables from Postgres to run through the machine learning model. We added this connection in the Batter and Pitcher RFC Model notebooks so we could pull the tables needed to run through the model. This was done by establishing a connection to the database with a cursor object, writing SQL statements to seelct the entirety of our tables, and saving them to a variable we could use moving forward. 

## Machine Learning Model

The ideal machine learning model for determining Baseball Hall of Fame inductees is one that has a high precision score, exemplifying the model's ability to make predictions that are correct (if predicted to be in Hall of Fame, how likely it is true).  In addition, the higher a recall score for the model, demonstrates the model's capability of finding worthy candidates for the Hall of Fame within a given dataset (finding a yes in a sea of no's).  Focusing on the model's ability to predict whether a player has been or will be inducted to the Hall of Fame is more important than the model's ability to predict if a player has not or will not be inducted into the Hall of Fame.  After testing various machine learning models and adjusting the parameters for the models, the results of two in particular should be compared.  

Prior to developing and running the machine learning models, the same preprocessing steps were applied to the dataset for each model:

* The **inducted** column is converted from values of Y and N, to 1 and 0 respectively- enabling the models to classify baseball players' inducted status numerically.
* The target variable, **y**, is assigned to the "inducted column".
* The features, **X**, is assigned to the remaining columns of baseball player stats.
* The assigned variables are then split into training and testing sets, utizlizing **train_test_split** from scikit-learn.
* Finally, **X** is then scaled so that all statistics within the datset fall within the same range of values, helping the model interpret the data more accurately.  

Once preprocessing the data was complete, the Random Forest Classifier and Logisitic Regression machine learning models were used to make predictions on baseball players being inducted into the Hall of Fame.  The Random Forest Classifier performed quite well initially with a 96.7% accuracy, 0.75 precision and 0.59 recall for being inducted into the Hall of Fame.  Adjustments were made to the sampling sizes in an effort to bring balance to the overwhelming amount of baseball players not inducted into the Hall of Fame.  Below are the results:


| Model and Sampling Method | Accuracy | Yes/No |Precision | Recall | F-1 Score | | | Confusion Matrix | |
| --------------- | -------- | ------ |--------- | ------ | --------- | - | - | - | - |
| *Random Forest Classifier (RFC)* | 96.7% | *No* | 1.00 | 1.00 | 1.00 | | | *Predicted No* | *Predicted Yes* |
| | | *Yes* | 0.71 | 0.59 | 0.65 | | *Actual No* | 4335 | 8 |
| | | | | | | | *Actual Yes* | 14 | 20 |
| *RFC with Random Oversampling* | 99.2% | *No* | 1.00 | 1.00 | 1.00 | | | *Predicted No* | *Predicted Yes* |
| | | *Yes* | 0.50 | 0.53 | 0.51 | | *Actual No* | 4325 | 18 |
| | | | | | | | *Actual Yes*| 16 | 18 |
| *RFC with Random Undersampling* | 95.3% | *No* | 1.00 | 0.95 | 0.98 | | | *Predicted No* | *Predicted Yes* |
| | | *Yes* | 0.14 | 1.00 | 0.25 | | *Actual No* | 4138 | 205 |
| | | | | | | | *Actual Yes* | 0 | 34 |
| *RFC with SMOTE* | 98.5% | *No* | 1.00 | 0.99 | 0.99 | | | *Predicted No* | *Predicted Yes* |
| | | *Yes* | 0.31 | 0.76 | 0.44 | | *Actual No* | 4285 | 58 |
| | | | | | | | *Actual Yes* | 8 | 26 |
| *RFC with SMOTEEN* | 98.2% | *No* | 1.00 | 0.98 | 0.99 | | | *Predicted No* | *Predicted Yes* |
| | | *Yes* | 0.28 | 0.82 | 0.42 | | *Actual No* | 4271 | 72 |
| | | | | | | | *Actual Yes* | 6 | 28 |
| *RFC with Cluster Centroids* | 98.1% | *No* | 1.00 | 0.98 | 0.99 | | | *Predicted No* | *Predicted Yes* |
| | | *Yes* | 0.27 | 0.88 | 0.41 | | *Actual No* | 4262 | 81 |
| | | | | | | | *Actual Yes* | 4 | 30 |
| *Logistic Regression* | 99.4% | *No* | 1.00 | 1.00 | 1.00 | | | *Predicted No* | *Predicted Yes* |
| | | *Yes* | 0.59 | 0.56 | 0.58 | | *Actual No* | 4330 | 13 |
| | | | | | | | *Actual Yes* | 15 | 19 |
| *Logistic Regression with 75% Threshold* | 99.4% | *No* | 0.99 | 1.00 | 1.00 | | | *Predicted No* | *Predicted Yes* |
| | | *Yes* | 0.71 | 0.35 | 0.47 | | *Actual No* | 4338 | 5 |
| | | | | | | | *Actual Yes* | 22 | 12 |

## Visualizations
Visualizations were created in Tableau to demonstrate how rare it is to be inducted to the Baseball Hall of Fame, and how it has become even more difficult to be competitive over time. A snapshot of these visualizations will be shown on the web app. 

## Deployment
For User-Facing purposes - a combination of 
- HTML 
- CSS 
- Bootstrap 
- JS 
- Python
- Flask has been utilized to build a dynamic webpage with current functionality to: 
	- Scrape the top article from the Basball Hall of Fame's website, as well as pictures from the Hall's image gallery
	- Create a dropdown list of Hall of Fame candidates throughout the history of baseball.
	- Additional functionality to be added shortly!

### Heroku 
Heroku is a cloud-based service that has the functionality to connect to Github, which creates automatic deployment of our project.  
Continuous code can be committed to the repository and then deployed within the Heroku platform by initially setting up the following files:
* h_app: is the app folder created to contain the flask app and supporting templates
	* __init__.py: the file that creates the flask app and additional routes
	*static: this is a folder created to hold javascript and CSS
		* CSS: a folder that contains the CSS functionality 
			* style.css: contains the styling for the app
		* JS: a folder that contains javascript files
			* script.js: this file creates the drop down functionality of baseball players
	* templates: the folder created within the app folder to organize html files
		* base.html: creates the initial structure for our webpage
		* index.html: an extension from our base.html and contains the main content
		* background.html: the route created to contain all the background information required for understanding the purpose of the project 
		* scrape.html: the route created to have all the scraping elements from the official Hall of Fame website
* Procfile: this is file specifically used for Heroku to create the webserver and initialize the starting point
* requirements.txt: this text file shows all the packages being used 
* wsgi.py: this file imports our flask app
* hof_scraping.py: contains all dependencies and functionality in order to pull the images from the baseball hall of fame website into our heroku app

## Credits

This project would not have been possible without the use of [Sean Lahman's Baseball Database](http://www.seanlahman.com/baseball-archive/statistics/), which is used here under the conditions of the
[Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/). Any changes made to the original database have been described in this README. Further use of 
this material is allowed under the same Creative Commons License.

“Homepage.” Baseball Hall of Fame, 23 Feb. 2021, baseballhall.org/. 
This resource was used to obtain the Baseball Hall of Fame logo that is presented at the top of this document. 
