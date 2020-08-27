# PostgreSQL INNER JOIN

## In order to combine data from multiple tables (actors, movies and directors):

- SELECT title, name, director from movies m inner join actors a on (a.knownfortitles = m.title)
inner join directors d on (m.title = d.knownfortitles);

## It is also possible to add another column and change a column name to a new representation:

- SELECT title, tags, name as Featuring, director from movies m inner join actors a on (a.knownfortitles = m.title)
inner join directors d on (m.title = d.knownfortitles);
