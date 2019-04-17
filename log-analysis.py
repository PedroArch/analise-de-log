#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2


# Create a dictionary of the most accessed posts
def most_accessed_posts():
    query_posts = """
                  SELECT articles.title, count(log.path) as total
                  FROM articles left join log
                  ON concat('/article/', articles.slug) = log.path
                  GROUP BY articles.title
                  ORDER BY total desc
                  LIMIT 3;
                  """
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query_posts)
    top_posts = c.fetchall()
    db.close()
    return top_posts


# Print out the most accessed posts
def first_request(most_accessed_posts):
    print("*" * 100)
    print("\n")
    print("MOST POPULAR THREE ARTICLES OF ALL TIME:")
    for (post, views) in most_accessed_posts:
        print("{} - {} views".format(post, views))
    print("\n")
    print("*"*100)


# Create a dictionary of the most accessed authors
def most_accessed_authors():
    query_authors = """
                    SELECT info_authors.name, count(log.path)
                    FROM info_authors
                    LEFT JOIN log
                    ON CONCAT('/article/',info_authors.slug) = log.path
                    GROUP BY info_authors.name
                    ORDER BY count(log.path) DESC
                    """
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query_authors)
    top_authors = c.fetchall()
    db.close()
    return top_authors


# Print out the most accessed authors
def second_request(most_accessed_authors):
    print("*" * 100)
    print("\n")
    print("MOST POPULAR ARTICLES AUTHORS OF ALL TIME:")
    for (authors, views) in most_accessed_authors:
        print("{} - {} views".format(authors, views))
    print("\n")
    print("*"*100)
    print("*"*100)


# Create a dictionary of days with requests that took more than 1% of errors
def percent_errors():
    query_percent = """
                    SELECT r.day, (100.0 * e.errors/r.requests) AS percetagem
                    FROM requests_day AS r
                    JOIN errors_per_day AS e
                    ON r.day = e.day
                    ORDER BY r.day;
                    """
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query_percent)
    percent = c.fetchall()
    db.close()
    return percent


# Print out days with requests that took more than 1% of errors
def third_request(percent_errors):
    print("*"*100)
    print("\n")
    print("DAYS MORE THAN 1% OF REQUEST LEAD TO ERRORS:")
    for (day, percenterror) in percent_errors:
            if percenterror > 1:
                print("{} - {} % errors".format(day, round(percenterror, 2)))
    print("\n")
    print("*"*100)


if __name__ == "__main__":

    # Question 1
    artigos_mais_acessados = most_accessed_posts()
    first_request(artigos_mais_acessados)

    # Question 2
    autores_mais_lidos = most_accessed_authors()
    second_request(autores_mais_lidos)

    # Question 3
    percent_errors = percent_errors()
    third_request(percent_errors)
