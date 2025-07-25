# Otimização de Produção e Distribuição Integrada com Múltiplas Plantas

Este repositório contém um modelo de otimização matemática para resolver um problema complexo de dimensionamento de lotes, produção e distribuição para uma indústria de embalagens de alumínio com múltiplas plantas e centros de distribuição na América do Sul.

## Contexto do Problema

O projeto aborda o desafio de uma empresa multinacional de latas de alumínio, que opera com produção contínua em diversas plantas e linhas de produção. O atendimento aos clientes é realizado tanto diretamente das fábricas quanto através de centros de distribuição externos.

O objetivo principal é criar um plano de produção e logística que minimize os custos totais de distribuição (frete e armazenagem) e, ao mesmo tempo, minimize o backlog (demandas não atendidas), garantindo que os produtos cheguem aos clientes nos períodos corretos.

### Principais Desafios e Restrições:
* **Produção:** A produção é limitada pela *capacidade* (taxa de produção e tempo disponível) e pela *capabilidade* (quais tipos de produtos uma linha consegue produzir em um determinado período).
* **Distribuição:** Clientes podem ser atendidos por diferentes rotas, cada uma com seu custo de frete e tempo de entrega (lead time) associados.
* **Armazenagem:** Tanto as plantas quanto os centros de distribuição possuem capacidade de armazenagem limitada e custos associados.
* **Demandas:** As demandas dos clientes são específicas por produto, cliente e período (dia) e devem ser atendidas sem atrasos. Demandas não atendidas no período são consideradas *backlog* e não podem ser postergadas.


# Otimização de Produção e Distribuição Integrada com Múltiplas Plantas

Este repositório contém um modelo de otimização matemática para resolver um problema complexo de dimensionamento de lotes, produção e distribuição para uma indústria de embalagens de alumínio com múltiplas plantas e centros de distribuição na América do Sul.

## Contexto do Problema

O projeto aborda o desafio de uma empresa multinacional de latas de alumínio, que opera com produção contínua em diversas plantas e linhas de produção. O atendimento aos clientes é realizado tanto diretamente das fábricas quanto através de centros de distribuição externos.

O objetivo principal é criar um plano de produção e logística que minimize os custos totais de distribuição (frete e armazenagem) e, ao mesmo tempo, minimize o backlog (demandas não atendidas), garantindo que os produtos cheguem aos clientes nos períodos corretos.

### Principais Desafios e Restrições:
* **Produção:** A produção é limitada pela *capacidade* (taxa de produção e tempo disponível) e pela *capabilidade* (quais tipos de produtos uma linha consegue produzir em um determinado período).
* **Distribuição:** Clientes podem ser atendidos por diferentes rotas, cada uma com seu custo de frete e tempo de entrega (lead time) associados.
* **Armazenagem:** Tanto as plantas quanto os centros de distribuição possuem capacidade de armazenagem limitada e custos associados.
* **Demandas:** As demandas dos clientes são específicas por produto, cliente e período (dia) e devem ser atendidas sem atrasos. Demandas não atendidas no período são consideradas *backlog* e não podem ser postergadas.

## Estrutura do Repositório


```
.
├── docs/                 # Documentação e apresentações do projeto
├── gerador/              # Scripts para gerar dados de exemplo (samples)
├── modelo/               # Código do modelo 
│   ├── sample_data/
│   ├── results/
│   ├── lotsizing_model.ipynb   # Modelo que considera custos unitários
│   └── lotsizing_model2.ipynb  # Modelo que considera custos por caminhão
├── modelo.ipynb          # Jupyter Notebook com a formulação matemática do problema
└── requirements.txt      # Dependências do projeto
```


## Como Utilizar

### 1. Pré-requisitos

Para executar os modelos e scripts, você precisará ter o Python 3 e as bibliotecas listadas no arquivo `requirements.txt` instaladas.

**Instalação das Dependências:**

1.  Crie e ative um ambiente virtual (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/macOS
    # ou
    .\venv\Scripts\activate   # Para Windows
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    *Observação: O modelo utiliza solvers de otimização como HiGHS e Gurobi, que são instalados via `pyomo` e `highspy`.*

### 2. Geração de Dados de Amostra

O repositório inclui um script para gerar dados de exemplo aleatórios, mantendo a consistência entre eles.

* Para gerar uma nova amostra, execute o script `generate_sample.py` dentro da pasta `gerador`:
    ```bash
    python gerador/generate_sample.py
    ```
* Novos arquivos de amostra em formato `.xlsx` serão criados na pasta `gerador/samples/`.

### 3. Execução do Modelo de Otimização

Os modelos de otimização estão implementados em Jupyter Notebooks:
* `lotsizing_model.ipynb`:Modelo que considera custos unitários
* `lotsizing_model2.ipynb`:Modelo que considera custos por caminhão
  
Para executar o modelo, abra um dos notebooks, carregue os dados de entrada (da pasta `sample_data/`) e execute as células. O resultado da otimização será salvo na pasta de resultados correspondente (ex: `model/results/`).

## Modelo Matemático

A formulação matemática do problema está detalhada no arquivo `modelo.ipynb`. Em resumo, o modelo busca:

**Minimizar:**
`Custo Total = (Custo de Frete) + (Custo de Armazenagem) + (Penalidade por Backlog)`

**Sujeito a Restrições de:**
* Capacidade e Capabilidade de Produção
* Balanço de Estoque nas Plantas e Centros de Distribuição
* Capacidade Máxima de Armazenagem
* Atendimento da Demanda (considerando lead times)
