# Estados Brasileiros API

A API de Estados Brasileiros é uma plataforma que fornece informações detalhadas sobre cada estado do Brasil. A API oferece uma variedade de endpoints que permitem aos desenvolvedores acessar facilmente informações sobre as unidades federativas brasileiras.

# Referências

Os dados apresentados pela API foram coletados no dia 15/11/2023 a partir do site do Instituto Brasileiro de Geografia e Estatística (IBGE). <br>Disponível em: <https://www.ibge.gov.br/cidades-e-estados/>.

# Motivação

Este projeto foi criado com único intuito de estudar sobre a criação e hospedagem de API's utilizando python.

# Tecnologias Utilizadas

* Python
* FastApi
* Uvicorn

# Instalando a API

Após realizar o fork ou baixar os documentos em seu computador alguns passos devem ser seguidores para utilizar a API.

1. Instalar os requisitos atráves do requirements.txt

Ao executar o seguinte comando todas as bibliotecas necessárias serão instaladas.

```
pip install -r requirements.txt
```

Obs: é recomendado a configuração de uma venv (ambiente virtual).

2. Subir uma instância local

No diretório raiz o seguinte código deve ser executado para acessar a api localmente.
```
uvicorn main:app --reload
```
Obs: a API geralmente estára disponível em <localhost:8000/>

3. Acessar a documentação

Para acessar a documentação da API basta após o passo anterior acessar <localhost:8000/docs>

# Rotas

A API possui 3 rotas:

* '/'

Está rota tem o intuito de mostrar uma mensagem que informa que a API está online.<br>

```
{
    "status": 200,
    "data": "API ESTADOS DO BRASIL ON"
}
```
<p align="center">Retorno rota '/'</p>

* '/estados'
Está rota trás para o usuário todos os estados brasileiros e suas respectivas unidades federativas (UF).

```
{
    "status": 200,
    "data": {
        1: {"uf": "AC", "estado": "Acre"},
        2: {"uf": "AL", "estado": "Alagoas"},
        3: {"uf": "AP", "estado": "Amapá"},
        ...
    }
}
```
<p align="center">Retorno rota '/estados'</p>

* '/estados/detalhes/{id}'
Está rota trás para o usuário detalhes específicos de um estado em questão atráves de um respectivo ID.

```
{
    "status": 200,
    "data": {
        1: {
            "uf": "AC", 
            "estado": "Acre", 
            "regiao": "Norte", 
            "capital": "Rio Branco", 
            "populacao": 830018, 
            "area_km2": 164173429, 
            "idh": 0.71,
            "fuso_horario": "GMT-5"
        },
        ...
    }
}
```
<p align="center">Retorno rota '/estados/detalhes/{id}'</p>

Obs: caso o ID informado não exista o retorno é:

```
{
    "status": 400,
    "data": "Identificador de estado inválido"
}
```