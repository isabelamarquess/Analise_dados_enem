# 📊 Análise Inicial de Dados de Participantes do ENEM

Este projeto tem como objetivo principal demonstrar o conhecimento em Python e Pandas através da manipulação e inspeção eficiente de um grande e desafiador conjunto de dados públicos: os registros de participantes do ENEM.

---

## 🛠️ Ferramentas e Tecnologias

O projeto utiliza o ecossistema Python para manipulação de dados:

* **Python:** Linguagem de programação.
* **Pandas:** Biblioteca essencial para leitura, manipulação e análise de dados tabulares (DataFrames).
* **Git:** Utilizado para versionamento do código.

---

## ✨ Funcionalidades do Código (`extract_data.py`)

O script `extract_data.py` executa as seguintes etapas:

### 1. Carregamento Otimizado de Dados

* **Arquivo Fonte:** `PARTICIPANTES_2024.csv`.
* **Contorno de `MemoryError`:** O código utiliza o parâmetro `usecols` para carregar **apenas as colunas necessárias** (`NU_INSCRICAO`, `NU_ANO`, `SG_UF_PROVA`, `TP_SEXO`), reduzindo drasticamente o consumo de memória, vital para arquivos com milhões de linhas.
* **Tratamento de Formato:** Utiliza `encoding='latin-1'` e `sep=';'` para corrigir problemas de acentuação (`UnicodeDecodeError`) e garantir a correta separação das colunas, comuns em datasets públicos brasileiros.

### 2. Inspeção Inicial 

Após o carregamento, o script realiza a inspeção básica do DataFrame:

* Exibe a estrutura completa do DataFrame com **`df.info()`**.
* Exibe as **5 primeiras linhas (`df.head()`)** e as **5 últimas linhas (`df.tail()`)** para verificar a integridade dos dados.

### 3. Análise e Filtragem Básica

O código demonstra uma técnica de análise de dados: a filtragem booleana.

* **Filtragem por UF:** Seleciona e exibe apenas os registros dos candidatos que realizaram a prova no **Rio Grande do Sul (`'RS'`)**.
* **Contagem:** Exibe o número total de participantes filtrados (`candidatos_rs.shape[0]`).

---

## ⚙️ Como Executar
* **Instale pandas:**
`pip install pandas`
* **Coloque o arquivo `PARTICIPANTES_2024.csv` no mesmo diretório.**
* **E então execute no terminal:**
`python extract_data.py`
