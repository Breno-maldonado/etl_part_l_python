# ETL Python - DummyJSON API 🚀

Este repositório contém um pipeline de **ETL (Extract, Transform, Load)** desenvolvido para demonstrar o fluxo de consumo, armazenamento e transformação de dados utilizando Python.

---

## 📝 Descrição do Projeto

O objetivo deste projeto é extrair dados semiestruturados de uma API pública ([DummyJSON](https://dummyjson.com/)), persistir esses dados em uma camada de "Raw" (dados brutos) e, posteriormente, transformá-los em arquivos estruturados (CSV) em uma camada "Curated".

## 🏗️ Estrutura do Repositório

Seguindo as melhores práticas de Engenharia de Dados, o projeto está organizado em camadas:

* **`raw/`**: Atua como uma *Landing Zone*. Aqui, os dados são salvos em formato `.json` exatamente como vêm da API, garantindo a linhagem dos dados brutos.
    * `/user`: Arquivos JSON de usuários.
    * `/products`: Arquivos JSON de produtos.
* **`curated/`**: Camada de dados prontos para negócio. Os dados são convertidos para `.csv` para facilitar o consumo por ferramentas de BI ou análise.
* **`main.py`**: O motor do projeto, contendo as funções de requisição, paginação e transformação com Pandas.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: Linguagem base.
* **Requests**: Para comunicação com a API REST.
* **Pandas & Numpy**: Para manipulação de DataFrames e conversão de formatos.
* **JSON**: Para persistência e leitura de arquivos semiestruturados.

## 🚀 Como Funciona

1.  **Extração**: A função `extracao_dados` realiza o consumo do endpoint específico.
2.  **Carga (Raw)**: O script percorre os IDs (limite de 10 por padrão) e salva cada registro como um arquivo individual na pasta `raw/`.
3.  **Transformação**: A função `transform_data_json_to_csv` lê o arquivo JSON, carrega-o em um DataFrame do Pandas e o exporta para a pasta `curated/` com a extensão CSV.
