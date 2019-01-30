#ANÁLISE DE LOGS

Você foi contratado(a) para um time que trabalha no site de um jornal. O frontend do site, e o banco de dados por trás dele, já estão feitos e em funcionamento. Pediram a você para construir uma **ferramenta interna de relatórios** (internal reporting tool) que usará informações do banco de dados para descobrir de que tipo de artigos os leitores do site gostam.

O banco de dados contém artigos de jornal, bem como o log do servidor web para o site. O log tem uma linha de banco de dados para cada vez que um leitor abre de uma página da web. Usando essa informação, seu código responderá a perguntas sobre a atividade do usuário do site.

O programa que você escreve neste projeto será executado na linha de comando. Nenhum input do usuário será necessário. Em vez disso, vai se conectar ao banco de dados, usar queries SQL para analisar os dados de log e imprimir as respostas a algumas perguntas.

##Para que serve esse projeto?
Neste projeto, você vai ampliar suas habilidades de banco de dados SQL. Você vai praticar interagindo com um banco de dados ao vivo, tanto da linha de comando como de seu código. Você vai explorar um grande banco de dados com mais de um milhão de linhas. E você vai construir e refinar queries complexas e usá-las para tirar conclusões de negócios a partir de dados.

##Geração de relatório
Construir um resumo informativo de logs é uma tarefa real que surge muitas vezes em engenharia de software. Por exemplo, no Udacity nós coletamos logs para ajudar-nos a medir progresso do aluno e o sucesso dos nossos cursos. As ferramentas de relatórios que usamos para analisar os logs envolvem centenas de linhas de SQL.

##Banco de dados como um recurso compartilhado
Neste projeto, você vai trabalhar com os dados que podem ter vindo de um aplicativo web do mundo real, com campos que representam informações que um servidor gravaria, tais como códigos de status HTTP e caminhos de URL. O servidor web e a ferramenta de relatório conectam, ambos, à mesma base de dados, permitindo que a informação flua de um servidor web ao relatório.

Isso mostra uma das valiosas funções de um servidor de banco de dados em um aplicativo do mundo real: é um ponto onde diferentes peças de software (um aplicativo da web e uma ferramenta de relatórios, por exemplo) podem compartilhar dados.


![Apenas uma das muitas queries que a Udacity usa para logs de análise.](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57bf410d_pasted-image-at-2016-08-24-18-22/pasted-image-at-2016-08-24-18-22.png)