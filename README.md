
# LOG ANALYSIS PROJECT - Udacity Full Stack Web Developer Nanodegree

## [DESCRIPTION](project-description.md)

For this project, my task was to create a reporting tool that prints out reports based on the given database. This Python program use the psycopg2 module to connect to the PostgreSQL database. As you run the program, it will introduce the answers, in plain text, to the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. Which days more than 1% of requests lead to errors?

#### [PROJECT RUBRICS](project-rubrics.md)


## REQUIREMENTS
- Python 3.7.1
- psycopg2
- Postgresql 9.6
- Winzip or 7-zip

## RUNNING THE PROGRAM


1. Download the database file [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

2. Extract the newsdata.zip file. This file should be inside the program folder.

3. Load the database using `psql -d news -f newsdata.sql`.

4. Connect to the database using `psql -d news`.

5. Create the Views given below. Then exit `\q`

6. Now execute the Python file - `python logs_analysis.py`.

## CREATED VIEWS

```sql
CREATE VIEW info_authors AS
SELECT authors.name, articles.title, articles.slug
FROM authors
JOIN articles ON articles.author = authors.id
ORDER BY authors.name;
```
```sql
CREATE VIEW errors_per_day AS
SELECT date(time) AS day , count(path) AS errors
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY day
ORDER BY day;
```
```sql
CREATE VIEW requests_day AS
SELECT date(time) AS day, count(*) AS requests
FROM log group by day
ORDER BY day;
```
