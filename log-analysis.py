#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2


# Cria o dicionário dos post mais acessados
def post_mais_acessados():
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


# Printa os post mais acessados
def primeira_requisicao(post_mais_acessados):
    print("*" * 100)
    print("\n")
    print("OS ARTIGOS MAIS ACESSADOS:")
    for (post, views) in post_mais_acessados:
        print("{} - {} views".format(post, views))
    print("\n")
    print("*"*100)


# Cria o dicionário dos artistas mais acessados
def autores_mais_acessados():
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
    top_autores = c.fetchall()
    db.close()
    return top_autores


# Printa os autores mais acessados
def segunda_requisicao(autores_mais_acessados):
    print("*" * 100)
    print("\n")
    print("OS AUTORES MAIS ACESSADOS:")
    for (autores, views) in autores_mais_acessados:
        print("{} - {} views".format(autores, views))
    print("\n")
    print("*"*100)
    print("*"*100)


# Cria o dicionário dos error por dia
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


# Printa os dias que tiveram mais de 1% das requições com erros
def terceira_requisicao(percent_errors):
    print("*"*100)
    print("\n")
    print("DIAS COM MAIS DE 1% DE ERROS NAS REQUISICOES")
    for (day, percenterror) in percent_errors:
            if percenterror > 1:
                print("{} - {} % erros".format(day, round(percenterror, 2)))
    print("\n")
    print("*"*100)


if __name__ == "__main__":

    # Questão 1
    artigos_mais_acessados = post_mais_acessados()
    primeira_requisicao(artigos_mais_acessados)

    # Questão 2
    autores_mais_lidos = autores_mais_acessados()
    segunda_requisicao(autores_mais_lidos)

    # Questão 3
    percent_errors = percent_errors()
    terceira_requisicao(percent_errors)
