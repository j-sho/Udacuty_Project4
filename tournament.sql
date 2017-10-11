-- Table definitions for the tournament project.

CREATE TABLE players (id SERIAL primary key, name TEXT);

CREATE TABLE matches (id_matches SERIAL primary key,
                      winner INTEGER REFERENCES players (id),
                      loser INTEGER REFERENCES players (id));

CREATE VIEW playerStandings AS
    SELECT  p.id, p.name,
            SUM(CASE WHEN p.id = m.winner THEN 1 ELSE 0 END) AS TotalWinnes,
            COUNT(m.id_matches) AS TotalMatches
    FROM players p LEFT JOIN matches m
    ON p.id = m.winner OR p.id = m.loser
    GROUP BY p.id
    ORDER BY TotalWinnes DESC,
             TotalMatches ASC;
