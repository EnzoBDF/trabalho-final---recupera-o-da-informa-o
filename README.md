# Comparativo de Modelos de Recuperação da Informação

Este projeto implementa e avalia um pipeline completo para comparar diferentes modelos de busca textual: **BM25**, **Gensim (TF-IDF)** e **Whoosh**.

O sistema é capaz de processar uma coleção de documentos em formato PDF, executar um conjunto de queries em cada modelo e, ao final, calcular métricas de avaliação (Precisão, Revocação e F1-Score) para determinar o desempenho de cada abordagem.



## Tecnologias Utilizadas

- **Python 3**
- **Bibliotecas Principais:**
  - `PyPDF2`: Para extração de texto de arquivos PDF.
  - `rank_bm25`: Para a implementação do modelo BM25.
  - `gensim`: Para a implementação do modelo TF-IDF.
  - `whoosh`: Para a implementação de um motor de busca completo.

## Estrutura do Projeto

- `data/`: Contém os dados de entrada.
  - `pdfs/`: Pasta para colocar os documentos PDF a serem processados.
  - `documents.txt`: Arquivo gerado com o texto extraído dos PDFs.
  - `queries.txt`: Lista de consultas a serem executadas.
  - `relevancia.json`: Mapeamento de quais documentos são relevantes para cada consulta.
- `models/`: Implementação dos diferentes modelos de busca.
- `evaluation/`: Scripts e métricas para avaliação dos resultados.
- `results/`: Armazena os resultados das buscas em formato JSON.
- `report/`: Local para o relatório comparativo final.

---

## Como Executar (Passo a Passo)

Para executar o projeto do início ao fim, **execute todos os comandos a partir do diretório raiz do projeto**.

### 1. Pré-requisitos

- Certifique-se de ter o **Python 3** instalado.

### 2. Instalação das Dependências

Instale todas as bibliotecas necessárias com um único comando:
```bash
pip install -r requirements.txt
```

### 3. Preparação dos Dados

1.  **Adicione seus PDFs**: Coloque todos os seus arquivos `.pdf` dentro da pasta `data/pdfs/`.
2.  **Extraia o Texto**: Execute o script para extrair o texto dos PDFs e gerar o `data/documents.txt`.
    ```bash
    python extract_pdfs.py
    ```
3.  **(Opcional) Customize as Buscas**:
    - Edite o arquivo `data/queries.txt` para definir suas próprias consultas (uma por linha).
    - Edite o arquivo `data/relevancia.json` para definir a relevância esperada para suas consultas.

### 4. Execução dos Modelos

Execute os scripts abaixo na ordem correta para construir os índices e gerar os resultados de busca para cada modelo.

#### Modelo BM25
```bash
python models/bm25_model/search.py
```

#### Modelo Gensim (TF-IDF)
```bash
# 1. Constrói o modelo
python models/gensim_model/build_model.py

# 2. Executa a busca
python models/gensim_model/search.py
```

#### Modelo Whoosh
```bash
# 1. Cria o índice
python models/whoosh_model/index.py

# 2. Executa a busca
python models/whoosh_model/search.py
```

### 5. Avaliação dos Resultados

Após gerar os resultados para todos os modelos, execute o script de avaliação para ver um comparativo das métricas:
```bash
python evaluation/avaliar_todos.py
```
O terminal exibirá a Precisão, Revocação e F1-Score para cada query em cada modelo, além das médias de desempenho.

## Análise das Métricas

- **Precisão (Precision)**: Dos resultados que o modelo retornou, quantos estavam corretos? (Foco em não trazer "lixo").
- **Revocação (Recall)**: De todos os resultados que eram relevantes, quantos o modelo encontrou? (Foco em não deixar nada importante de fora).
- **F1-Score**: Uma média harmônica entre Precisão e Revocação. É a melhor métrica para avaliar o equilíbrio geral de um modelo.

---

## Licença

Este projeto está sob a licença MIT.
