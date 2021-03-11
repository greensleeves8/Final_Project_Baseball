Database:
Once ETL was pretty finalized we worked on putting the dataframes created (career_batter_df, hall_batter_df, career_pitching_df, hall_pitching_df) into a local postgreSQL database. In the jupyter notebook file we created the connection by importing create_engine from sqlalchemy, connecting with a connection string and database engine, and then importing each table. Once that was set up, we were able to pull these tables from postgres into our machine learning model. We initially had our machine learning model in a Jupyter Notebook file, so in that file we created a connection to the database with a cursor object, which allows you to traverse over the rows in the table, and in our case return the entire table to run through the model. Now that you know how we started this process, we're gonna go over our live web app, and after that you'll see how we calculated all of the information you're about to see. 

Future Advancements Thanks Questions:

Our project is just the beginning of what you could do to predict and analyze sports data. We would like to expand this product to help coaches of all sports take an objective look at their players and assure that all of the high performance players are not overlooked. 
- We could expand to other sports and their repsective awards, and predict who is going to be on all star teams in any sport. 
- Would love to have more interative pieces, possibly where you could put in someone's stats to see the probability of them being inducted, as well as looking at future predictions.
- Clean up CSS style and make webpage as clean as possible
