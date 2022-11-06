# BusHack
## 🐍 API Rest com FastAPI e PostgreSQL

Esta API foi desenvolvida pensando nos problemas que tem nas filas dos ônibus da UFPEL, e com ela aliada a uma interface gráfica(Site, Aplicativo, …) pode nos ajudar com as seguintes coisas:

- Ultima localização do ônibus
- Quantidades de pessoas no ônibus
- Quantidade de pessoas interessadas na rota do ônibus
- Histórico dos das rotas dos ônibus

## Como rodar a API?

Para começar temos que ver se temos essas dependências

### Dependências

- [Python3.11](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Makefile](https://pt.wikipedia.org/wiki/Makefile)

Após notarmos que temos todas as temos todas as dependências criaremos um arquivo .env como o arquivo [.env.example](./meache/.env.example), mas é claro com os seus dados.

Logo após isso executaremos esses comandos:
```shell
    $ poetry shell
    $ poetry install
    $ make run
```
## Referência:

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
