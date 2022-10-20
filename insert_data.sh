#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.
Echo $($PSQL "TRUNCATE teams, games RESTART IDENTITY")

#read file
cat games.csv | while IFS="," read YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
# Ignore first line
  if [[ $YEAR != "year" ]]
  then
    # Get team ids

    # Get winner_id:
    WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")
    
    # If not found:
    if [[ -z $WINNER_ID ]]
    then
      ADDED_TEAM=$($PSQL "INSERT INTO teams(name) VALUES('$WINNER')")
        
        # Echo to terminal:
        if [[ $ADDED_TEAM = "INSERT 0 1" ]]
        then
          echo Added $WINNER to teams
        fi
    fi

    # Get opponent_id:
    OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT'")
    
    # If not found:
    if [[ -z $OPPONENT_ID ]]
    then ADDED=$($PSQL "INSERT INTO teams(name) VALUES('$OPPONENT')")
      
      # Echo to terminal
      if [[ $ADDED = "INSERT 0 1" ]]
      then
        echo Added $OPPONENT to teams
      fi
    fi

  fi
done
cat games.csv | while IFS="," read YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER'")
  OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT'")

  if [[ $YEAR != "year" ]]
  then
    INSERT_G=$($PSQL "insert into games(year, round, winner_id, opponent_id, winner_goals, opponent_goals) 
    values ($YEAR, '$ROUND', $WINNER_ID, $OPPONENT_ID, $WINNER_GOALS, $OPPONENT_GOALS)")
  fi

  echo $YEAR, $ROUND $WINNER_ID, $OPPONENT_ID, $WINNER_GOALS, $OPPONENT_GOALS are in games now
done

