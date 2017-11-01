# Webcasts for the Tournament Results Project

This project includes a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament in a Swiss style (without elimination).

# Files

- `tournament.sql` - creates the database (tables and view)
- `tournament.py` - contains a number of functions to access and change the database
- `tournament_test.py` - contains a number of test functions

# Required Libraries

- psycopg2

# How to run

1. Log into your web server via SSH and be sure to have Python 2 and PostgreSQL installed (`vagrant up`, `vagrant ssh`)
2. Run `sudo apt-get update`
       `sudo apt-get install postgresql postgresql-contrib`
3. Initialize the database using `psql`
4. Run `\i tournament.sql`
5. Quit PostgreSQL with `\q`
6. Run python `tournament_test.py` to ensure correct initialization

# Functions in tournament.py

- `connect()` connects to the database
- `deleteMatches()` deletes all matches from the database
- `deletePlayers()` deletes all players from the database
- `countPlayers()` counts the number of registered players
- `registerPlayer(name)` adds a player to the tournament database
- `playerStandings()` outputs the list of registered players ordered by total wins
- `reportMatch(winner, loser)` records the outcome of a single match between two players
- `swissPairings()` returns a list of pairs of players for the next round of a match.
