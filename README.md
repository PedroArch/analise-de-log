
#Projeto Análise de Logs

## [Descrição do Projeto](Descicao-Projeto.md)
## [Rubricas do Projeto](Rubricas-Projeto.md)

##Questões
1. **Quais são os três artigos mais populares de todos os tempos?** Quais artigos foram os mais acessados? Apresente esta informação como uma lista organizada com o artigo mais popular no topo.
2. **Quem são os autores de artigos mais populares de todos os tempos?** Isto é, quando você organizar todos os artigos que cada autor escreveu, quais autores obtiveram mais views? Apresente esta informação como uma lista organizada com o autor mais popular no topo.
3. **Em quais dias mais de 1% das requisições resultaram em erros?** A tabela de logs inclui um status de coluna que indica o código de status HTTP que o site de notícias enviou ao navegador do usuário (consulte novamente esta aula se você quiser rever a ideia dos códigos de status HTTP).

##Requisitos
- Python 3.7.1
- psycopg2
- Postgresql 9.6

##Como executar

- Extraia os dados no banco de dados
````sql
psql -d news -f newsdata.sql
````
- Conecte ao banco de dados
````sql
psql news
````
* Crie as views com os codigos abaixo na seção VIEWS CRIADAS
* execute no console (certifique-se de estar na mesma pasta dos arquivos)
````buildoutcfg
python AnaliseLog.py
````

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