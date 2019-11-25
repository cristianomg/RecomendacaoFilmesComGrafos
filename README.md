# RecomendacaoFilmesComGrafos

O objetivo do sistema é recomendar filmes para um determinado usuário a partir dos filmes avaliados pelo mesmo. Para isso foi utilizado a base de dados Small de 100.000 ratings, disponibilizada pela MovieLens. Essa base de dados possui quatro arquivos em formato csv são eles:

* links: Nesse arquivo possui atributos dos filmes tais como id do mdbId e tmdbId, com esses ids é possivel ser feita consulta nas apis do Open Movie Database e The Movie Database para coletar informações como link de poster do filme, sinopse, diretor, atores.

* Movies: Nesse arquivo possui algumas informações do filme tais como nome do titulo e generos.

* Ratings: Nesse arquivo possui as avaliações de cada usuário para determinado filme que o mesmo avaliou.

* Tags: Nesse arquivo possui algumas tags relacionadas aos filmes porem o mesmo não foi utilizado no desenvolvimento do sistema.

## Let's go to Code

Primeiramente foi criado um script para fazer um agrupamento de filmes por usuário a partir do Arquivo Ratings.csv, esse script está contido no arquivo leituraBaseRatings.py. Caso queira utilizar uma base nova, modifique o caminho do arquivo ratings desejado e execute o script usando o comando (py leituraBaseRatings.py) dentro da pasta onde o arquivo está contido.

Com o arquivo users.json criado, podemos partir para o mapeamento do grafo. Para mapear o grafo foi criado um script chamado de verificarAdjacentes.py o qual verifica para cada usuário os usuários que possuem uma quantidade maior que 10 filmes que foram avaliados por ambos, com isso é aplicada o calculo da distancia euclidiana para os filmes que ambos avaliaram, o resultado desse calculo é o peso da aresta que possui os vertices os dois usuários analisados. Só serão inseridos no grafo arestas que possuam o peso menor que a media dos pesos por usuário (Vertice).

Com o grafo mapeado, foi feito um pequeno script que faz a leitura dos arquivos movies e links e cria um objeto para cada filme com as informações dos 2 arquivos, esse script está contido no arquivo criarJsonFilmes.py.

A leitura dos arquivos json criados anteriormente são realizadas pelo modulo leituraJson.py

### Recomendação do filme

As recomendações dos filmes é realizada por um algoritmo do menor caminho (Dijkstra) modificado, a modificação foi feita pois como possuem muitas arestas o algoritmo iria levar um custo muito alto para finalizar, com isso, a modificação consiste após armazena 16 filmes o algoritmo para.

#### Backend

Com o algoritmo de recomendação feito, foi criada uma aplicação em flask que possui 3 endpoints do tipo GET

* /user/id :  Esse primeiro endpoint retorna True caso o usuário informado está presente na base de dados;

* /users/id : Esse segundo endpoint retorna os 16 filmes melhores avaliados pelo usuário informado;

* /recomendacao/id : Esse terceiro endpoint retorna os 16 filmes recomendados pelo algoritmo de dijkstra Modificado, para o usuário informado.

A api está hospedada no pythonAnywhere e pode ser acessada pelo link: <https://cmacedog.pythonanywhere.com> utilizando os endpoints informados.

Para executar localmente instale as dependencias contidas no arquivo requirements.txt, após instaladas execute o arquivo app.py

#### Frontend

A parte visual do sistema foi feita em ReactJs e possui 2 endpoints:

* / : Esse endpoint é um formulario q solicita o id do usuário e envia o mesmo para o backend, consumindo o endpoint /user/id, caso o mesmo retorne True o usuário é navegado para o segundo endpoint.

* /dashboard : Nesse endpoints é listado os filmes avaliados pelo usuário e os filmes recomendados para o mesmo.

O frontend está hospedado no Heroku e pode ser acessado pelo link: <https://recommendermovies.herokuapp.com>

para executar localmente, certifique-se de que a api está no ar, instale as dependencias utilizando o comando npm install, após as dependencias instaladas utilize o comando npm start
