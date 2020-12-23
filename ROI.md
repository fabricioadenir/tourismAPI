<img src="docs/roi.png" width="123px" alt="verifica.me" align="right">

# sbturAPI

# v0.1.0

## Configuração e inicialização usando Docker.
Esse ambiente foi preparado para ser instalado no Docker seguindo os passos abaixo e o banco de dados PostGreSQL:

* Comando responsável pela criação da imagem e subir a API e o PostGreSQL.
```
docker-compose up -d --build
```

## Instalação e configuração ambiente local (Dev).
***
Depende de:
* [Python 3](https://www.python.org/downloads/) (3+).
* [PostGreSql](https://www.postgresql.org/download/windows/)
* [Docker](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

Se for utilizado o Docker para criar a imagem do PostGreSQL.

* O banco de dados PostGreSQL pode ser construido através do docker-compose com o seguinte comando.
```
docker-compose up -d --build --no-deps db
```

Caso não opte em utilizar o Docker:
1. Baixar o [PostGreSql](https://www.postgresql.org/download/windows/)
2. Criar os usuários default:
***Usuário default*** 'sbtur'
***Senha default*** 'sbtur_pwd'
3. Por default os arquivos de condiguração já estão com usuário e porta padrão do DB.

4. Instalar as dependências.
```sh
$ pip install -r requirements.txt
```

5. Montar a migração para o banco de dados.
```sh
$ python manage.py makemigrations
```

6. Realizar a migração da estrutura de dados para o banco.
```sh
$ python manage.py migrate
```

7. Criar alguns dados fictícios para testar a API.
```sh
$ python manage.py loaddata initial.json
```

8. Criação de usuário para que seja possível acessar o admin do Django.
```sh
$ python manage.py createsuperuser --email admin@example.com --username admin
```
***Obs***: O usuário criado será admin podendo escolher outro a seu critério.

9. Subir a API.
```sh
$ python manage.py runserver
```

&nbsp;

# EndPoit e como usar:

* http://localhost:8000/docs

## Contato


[Fabricio Silva](mailto:fabricioadenir@gmail.com)