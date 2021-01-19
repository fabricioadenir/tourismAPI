# tourismAPI

# v0.1.0

# EndPoint da documentação Swagger.
**Disponível todos os endpoint**

* http://localhost:8000/docs 

# Exemplo de uso.


**EndPoint disponiveis:**

1. Lista de categorias:
    * http://localhost:8000/categorias

2. Lista de cidades:
    * http://localhost:8000/cidades

3. Lista de paises:
    * http://localhost:8000/paises

4. Lista de hoteis:
    * http://localhost:8000/hoteis

5. Lista de rotas:
    * http://localhost:8000/rotas

6. Lista de vitrines:
    * http://localhost:8000/vitrines


# Como solicitado um filtro por rotas na vitrines cadastradas.

http://localhost:8000/vitrines/ method GET

#### Listagem das vitrines para página `/`

- Enviar como payload um array { "routes": ["/"] }
- Como mostra a imagem.
![ ](https://github.com/fabricioadenir/tourismAPI/blob/main/docs/barra.png?raw=true)

#### Listagem das vitrines para página `/destinos`

- Enviar como payload um array { "routes": ["/destinos"] }
- Como mostra a imagem.
![ ](https://github.com/fabricioadenir/tourismAPI/blob/main/docs/destinos.png?raw=true)


#### Listagem das vitrines para página `/sobre`

- Enviar como payload um array { "routes": ["/sobre"] }
- Como mostra a imagem.
![ ](https://github.com/fabricioadenir/tourismAPI/blob/main/docs/sobre.png?raw=true)