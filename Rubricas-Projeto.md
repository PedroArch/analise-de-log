#RUBRICAS DO PROJETO

##Funcionalidade

###Funcionalidade
- Rodar o código exibe as respostas corretas para cada uma das perguntas na descrição do lab.
###Compatibilidade: banco de dados
- O código funciona com o esquema de banco de dados. Não há problemas em adicionar views ao banco de dados, mas você não deve modificar ou renomear as tabelas existentes.
###Compatibilidade: linguagem
- O código pode ser escrito em Python 2 ou Python 3, mas deve ser consistente. Deveria começar com uma linha shebang correta para indicar a versão do Python.
###Saida de texto bem formatada
- O código apresenta sua saída em um documento de texto puro claramente formatado. Imagine que você está olhando este texto em uma mensagem de e-mail, não em uma página web.
###Queries do banco de dados
- O código se conecta a um banco de dados de SQL e faz queries nele. Não utiliza respostas hardcoded no código da aplicação.

##Qualidade do código

###Nenhum erro
- O código do projeto roda sem nenhuma mensagem de erro ou avisos de um interpretador de linguagem.
###Estilo do código da aplicação
- O código está de acordo com as recomendações de estilo do PEP8.
- Você pode instalar a ferramentapycodestyle para testar isso com pip install pycodestyle ou pip3 install pycodestyle (Python 3).
- Para ser aprovado neste requisito, rodar a ferramenta pycodestyle em seu código não deve gerar nehuma advertência. (pycodestyle era formalmente conhecido como pep8. Eles são a mesma coisa.)
###Qualidade do código SQL
- Quando o aplicativo obtém dados de diversas tabelas, ele usa uma única query com uma join, em vez de diversas queries. Cada uma das perguntas deve ser respondida usando uma query de SQL.

##Arquivo README

###Arquivo README descrevendo on trabalho
- O arquivo README inclui instruções sobre como rodar o programa, bem como uma descrição do projeto do programa.
- Imagine uma pessoa que sabe Python e SQL bem, mas não fez este projeto. Se ela lesse o README, saberia rodar este código?

###Arquivo README deve conter todas declaroçoes de create views
- Caso o código faça uso de views criadas no banco de dados, o arquivo README inclui as declarações create view das mesmas (se o código não utiliza views, ignore este item).