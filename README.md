<img src="docs/sbtur.png" width="123px" alt="verifica.me" align="right">

# sbturAPI

# v0.1.0

Esta API é responsável por implementar vitrines de promoções, possibilitando cadastros de promoções e suas alterações necessárias.

**Instalação e configuração** [ROI](https://github.com/fabricioadenir/sbturAPI/blob/master/ROI.md)

***
Depende de:
* [Python 3](https://www.python.org/downloads/) (3+).
* [PostGreSql](https://www.postgresql.org/download/windows/)
* [Docker](https://hub.docker.com/editions/community/docker-ce-desktop-windows) Caso deseje usar.

# Subindo API com docker:
Docker é responsável pela construção da API e PostGreSQL.

* Comando para criação e execução.
```
docker-compose up -d --build
```
&nbsp;
## Painel Django Rest para utilizar de forma direta na API (Precisa Autenticar).

* Exemplo: http://IP:PORT por default é: http://localhost:8000

&nbsp;
## Painel Admin do Django (Somente em modo DEBUG)

* Seguindo o exempo: http://localhost:8000/admin

&nbsp;

# EndPoit e como usar:
Para facilitar o uso e exemplicar como a API trabalha [clique aqui](https://github.com/fabricioadenir/sbturAPI/blob/main/docs/DOC.md) e veja a documentação de uso.

&nbsp;
# Executar testes
```sh
$ python manage.py test api/tests --verbosity 2
```

&nbsp;

# Lint
```sh
$ flake8 --config=flake8
```
```sh
$ pycodestyle --config=pycodestyle .
```

## Contato


[Fabricio Silva](mailto:fabricioadenir@gmail.com)