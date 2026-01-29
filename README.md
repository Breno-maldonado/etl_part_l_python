# Projeto ETL - Integração DummyJSON

Este repositório contém um pipeline de **ETL (Extract, Transform, Load)** desenvolvido em Python para demonstrar o consumo de APIs REST e a organização de dados em camadas (Raw e Curated). O projeto foca na extração de dados de usuários e produtos para posterior conversão e análise.

## 🏗️ Estrutura de Pastas

O projeto utiliza uma estrutura organizada para garantir a rastreabilidade dos dados em diferentes estágios de processamento:

* **raw/**: Camada de dados brutos, onde os arquivos `.json` são persistidos exatamente como recebidos da API.
* **curated/**: Camada de dados transformados, onde os arquivos são convertidos para `.csv` para facilitar o consumo em ferramentas de Analytics.
* **main.py**: Script principal que orquestra as funções de extração, carga e transformação.

## 🛠️ Tecnologias e Ferramentas

* **Linguagem**: Python.
* **Bibliotecas**: 
    * `Pandas` e `Numpy` para manipulação e estruturação de dados.
    * `Requests` para integração com APIs REST.
* **Formato de Dados**: JSON (entrada) e CSV (saída).

## 🚀 Fluxo do Pipeline

O pipeline está dividido em três etapas principais:

1.  **Extração**: O script consome os endpoints da API `dummyjson.com`.
2.  **Carga (Raw)**: Os dados são salvos localmente em formato JSON dentro da pasta `raw/`, respeitando o ID de cada registro.
3.  **Transformação (Curated)**: Os arquivos brutos são lidos, processados via DataFrame e convertidos para CSV na pasta `curated/`.
