
#Projeto Análise de Logs

##Objetivos
- Imprimir os três artigos mais populares de todos os tempos
- Imprimir os autores de artigos mais populares de todos os tempos
- Imprimir  quais dias mais de 1% das requisições resultaram em erros

##Como executar o programa
  Basta executar no prompt de comando o arquivo final_project.py digitando:
  >>python final_project.py

##Como cheguei aos resultados
  Quanto ao primeiro item criei no banco de dados uma coluna com o id dos artigos como uma chave estrangeira ligando a tabela de log a tabela de artigos
  >>alter table log add column id_article
  >>update log set id_article = (**numero do id do artigo na tabela articles**) where path like '(**utilizei uma palavra chave do path que continha somente nesse path**)';

  Quanto ao segundo item fiz o mesmo que no primeiro criando um id chave estrangeira dos autores no log
  >>alter table log add column id_author
  >>update log set id_author = (**numero do id do autor na tabela authors**) where path like '(**utilizei uma palavra chave do path que continha somente nesse path e que o artigo foi escrito pelo autor em questão**)';

  Quanto ao terceiro item usei funções que extraiam os dicionários com os dias e total de requisições e erros, então só implementei o calculo com condições de imprimir somente quando havia uma margem maior que 1% de erro nas requisições.

##VIEWS CRIADAS

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
```sql
CREATE VIEW percent_errors AS 
SELECT r.day, (100.0 * e.errors/r.requests) AS percetagem 
FROM requests_day AS r 
JOIN errors_per_day AS e ON r.day = e.day
ORDER BY r.day;
```