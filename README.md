# WeekFM

Twitta seus 5 artistas mais tocados na semana.

Roda localmente, com um schedule shell. 

## Tecnologias
Desenvolvido em python.

Utiliza [pylast](https://github.com/pylast/pylast) e [python-twitter](https://github.com/bear/python-twitter).

## Configurando

Você deve ter as duas chaves da API do [Last.fm](https://www.last.fm/pt/home), 
para obte-las acesse a [API](https://www.last.fm/api/account/create) do Last.fm 

Também deve-se ter as chaves da API do twitter,
pode-se obte-las [aqui](https://developer.twitter.com/en/apps)

Clone o projeto.

Após conseguir as chaves, configure suas informações em .env utilizando ` cp .env.example .env `

Para rodar o projeto ative o ambiente virtual ` pipenv shell ` (Caso não tenha o pipenv instalado, instale-o)
e execute ` python weekfm.py ` 

(Schedule ainda não implementado)

## Contribuindo 

Abra uma issue, fork o repositório e mande um pull request
