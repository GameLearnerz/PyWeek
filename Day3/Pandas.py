import pandas as pd

# # #Task1


# #Load CSV file into DataFrame.

df=pd.read_csv('ipl-matches.csv')

# #Display first 5 rows.

# print(df.head())

# #Show no. of rows and columns.

# print(df.shape)

# # #Task2


# #List all unique seasons and teams.

# print(df['Season'].unique()) #List all unique Seasons.
# print(df['Team1'].unique())  #List all unique teams in Team1.
# print(df['Team2'].unique())  #List all unique teams in Team2.

# #How many matches were played in each season?

# print(df['Season'].value_counts())

# #Which team won the most matches?

# print(df['Winner'].value_counts().head(1))

# # #Task3


# #Show matches where Mumbai Indians were the winner.

# print(df['WinningTeam'][df['WinningTeam']=='Mumbai Indians'])

# #Show all matches that went to super over.

# print(df[df['SuperOver']=='Y'])

# #Show matches held at "Eden Gardens".

# print(df[df['Venue']=='Eden Gardens'])

# # #Task4


# #How many super overs have been played in total?

# print(df[(df['SuperOver']=='Y')].agg({'SuperOver':'count'}))

# #Check if toss winner is also a match winner in percentage.

# print(((df[(df['TossWinner'])==(df['WinningTeam'])]).shape[0]/df.shape[0])*100)

