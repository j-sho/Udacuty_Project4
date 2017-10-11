# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(id) AS num FROM players;")
    countResult = int(cursor.fetchone()[0])
    db.close()
    return countResult


def registerPlayer(name):
    """Adds a player to the tournament database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM playerStandings;")
    result = cursor.fetchall()
    db.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s);",
                   (winner, loser))
    db.commit()
    db.close()



def swissPairings():
    """Returns a list of pairs of players for the next round of a match."""
    pairs = []
    tuple = playerStandings()
    for i in range(0, (len(tuple)-1), 2):
        pairs = pairs + [(tuple[i][0], tuple[i][1], tuple[i+1][0],
                         tuple[i+1][1])]
    return pairs
