# Boas-vindas ao repositório do Job Insights!

<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />
  <p align="center">
    <img src="/.images/job.png" alt="Logo Aplicação" width="300"/>
  </p>
  
  Neste projeto você implementará análises a partir de um conjunto de dados sobre empregos.

  Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

  🚵 Habilidades a serem trabalhadas:
  <ul>
    <li>Utilizar o terminal interativo do Python.</li>
    <li>Utilizar estruturas condicionais e de repetição.</li>
    <li>Utilizar funções built-in do Python.</li>
    <li>Utilizar tratamento de exceções.</li>
    <li>Realizar a manipulação de arquivos.</li>
    <li>Escrever funções.</li>
    <li>Escrever testes com Pytest.</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos.</li>
  </ul>
</details>

# Orientações
<details>
  <summary><strong>⚠ Antes de começar a desenvolver</strong></summary><br />

  1. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

# Requisitos Obrigatórios

## 1 - Count Ocurrences (Testes)
> **Implemente em:** `tests/counter/test_counter.py`

  <p align="center">
    <img src="/.images/flask.png" alt="Imagem sobre contar ocorrências" width="600"/>
  </p>

A empresa cliente contratou um relatório que informa a quantidade de ocorrências das palavra *Python* e *Javascript* nos dados e, para isso, temos uma implementação pronta em `src/pre_built/counter.py`. Durante o desenvolvimento, sofremos com alguns `bugs`, que já foram resolvidos. Para termos certeza e confiança da nossa entrega, no entanto, e não corrermos riscos, precisaremos de *testes automatizados* que garantam isso!

O nome deste teste **deve** ser `test_counter`, e ele deve garantir que atenda estas especificações:

- **Chamar** a função `count_ocurrences` passando dois parâmetros:
  - `path` uma string com o caminho do arquivo (`data/jobs.csv`);
  - `word` uma string com a palavra a ser contabilizada;
- Garantir que a função retorna corretamente a quantidade de ocorrências da palavra solicitada;
  - A contagem de palavras deve ser _case insentitive_, ou seja, não diferenciar letras maiúsculas de minúsculas;

## 2 - Implemente o método `read`
> **Implemente em:** `src/insights/jobs.py`

**Preparando para Processar Dados de Arquivos CSV com a Classe `ProcessJobs`**

O cliente ficou muito satisfeito com o excelente trabalho que você realizou, implementando todos os testes solicitados. Agora, eles estão empolgados para dar continuidade a um de seus projetos. A próxima etapa envolverá o processamento de dados contidos em arquivos CSV.

A classe ProcessJobs é fundamental nesse contexto, pois é responsável por lidar com operações relacionadas à leitura e processamento de dados sobre trabalhos a partir de um arquivo CSV. A classe apresenta métodos que permitem ler os dados de um arquivo CSV, obter tipos únicos de trabalhos e filtrar os trabalhos com base em seus tipos.

Antes de iniciar vamos compreender a funcionalidade da classe ProcessJobs. O código encontra-se no arquivo `src/insights/jobs.py`. Neste arquivo, você encontrará a implementação da classe ProcessJobs, que contém métodos específicos para realizar tarefas detalhadas, de acordo com os requisitos a seguir:

-----

Para começarmos a processar os dados, devemos antes carregá-los em nossa aplicação. E o método `read` será responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários. 

- O método deve receber um _path_ (uma string com o caminho para um arquivo).
- O método deve abrir o arquivo e ler seus conteúdos.
- O método deve tratar o arquivo como CSV.
- O método read deve ler o csv e armazenar os dados em `self.jobs_list`, que será lista dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha. 

## 3 - Implemente o método `get_unique_job_types`
> **Implemente em:** `src/insights/jobs.py`

Agora já temos como carregar os dados e podemos começar a extrair informação deles. Primeiro, vamos identificar quais tipos de empregos existem.

- A função deve retornar uma lista de valores únicos presentes na coluna `job_type`.

## 4 - Implemente o método `filter_by_multiple_criteria`
<p align="center">
  <img src="/.images/filter.png" alt="Contagem" width="400"/>
</p>

> **Implemente em:** `src/insights/jobs.py`

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa usuária possa filtrar os empregos por tipo de emprego, vamos precisar implementar mais um método na nossa classe `ProcessJobs`.

- O método deve receber uma lista de empregos representados por dicionários.
- Deve receber um dicionário filter_criteria que contém pares chave-valor, onde a - chave é o critério de filtragem (`industry` ou `job_type`) e o valor é o valor associado a esse critério.
- O método deve retornar uma lista de empregos que correspondem a todos os critérios fornecidos.

Exemplo do tipo de dado que o primeiro parâmetro do nosso método pode receber:

```python

jobs = [
    {"id": 1, "industry": "IT", "job_type": "FULL_TIME"},
    {"id": 2, "industry": "Healthcare", "job_type": "PART_TIME"},
    {"id": 3, "industry": "Finance", "job_type": "FULL_TIME"},
    {"id": 4, "industry": "IT", "job_type": "CONTRACTOR"},
    {"id": 5, "industry": "Healthcare", "job_type": "FULL_TIME"},
    {"id": 6, "industry": "Finance", "job_type": "PART_TIME"},
    {"id": 7, "industry": "IT", "job_type": "FULL_TIME"},
    {"id": 8, "industry": "Healthcare", "job_type": "CONTRACTOR"},
]
```
Exemplo de uso dos métodos:
```python

process_jobs = ProcessJobs()

# Filtrar por indústria "Healthcare" e tipo de emprego "PART_TIME"
result_by_multiple_criteria = process_jobs.filter_by_multiple_criteria(
    jobs, {"industry": "Healthcare", "job_type": "PART_TIME"}
)
```
## 5 - Implemente o método `get_unique_industries`
> **Implemente em:** `src/insights/industries.py`

Agora iremos identificar quais indústrias estão representadas nesse conjunto de dados. Para facilitar o trabalho, a outra pessoa desenvolvedora envolvida no projeto já deixou a classe `ProcessIndustries` implementada herdando a classe `ProcessJobs`. 

- O método deve retornar uma lista de valores únicos presentes na coluna `industry`.
- O método desconsidera valores vazios.

## 6 - Implemente o método `get_max_salary`
> **Implemente em:** `src/insights/salaries.py`

Dentro do arquivo mencionado, você encontrará a classe `ProcessSalaries`.

O método  `get_max_salary` deve extrair o maior salário dos dados que foram lidos e armazenados previamente na lista `self.jobs_list`. A classe `ProcessSalaries` herda funcionalidades da classe `ProcessJobs`, o que inclui a capacidade de acessar dados previamente lidos sem a necessidade de uma nova leitura do arquivo. 

Os dados contêm informações sobre as faixas salariais de cada emprego apresentado. Agora, nossa tarefa é identificar o valor mais alto entre todas essas faixas.

- O método deve ignorar os valores ausentes.
- O método deve retornar *um valor inteiro* com o maior salário presente na coluna.`max_salary`.

## 7 - Implemente o método `get_min_salary`
> **Implemente em:** `src/insights/salaries.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o menor valor de todas as faixas.

O método  `get_min_salary` deve extrair o menor salário dos dados que foram lidos e armazenados previamente na lista `self.jobs_list`.

- O método deve ignorar os valores ausentes.
- O método deve retornar *um valor inteiro* com o menor salário presente na coluna `min_salary`.

## 8 - Implemente o método `matches_salary_range`
> **Implemente em:** `src/insights/salaries.py`

O aplicativo vai precisar filtrar os empregos por salário também. Implemente o método `matches_salary_range` para conferir que o salário procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar também para conferir se a faixa salarial faz sentido -- isto é, se o valor mínimo é menor que o valor máximo.

- O método deve receber um dicionário `job` como primeiro parâmetro, com as chaves `min_salary` e `max_salary`, que podem ser números ou strings que representem números.
- O método  deve receber um número ou string que represente o número `salary` como segundo parâmetro.
- O método deve lançar um erro `ValueError` nos seguintes casos:
  - alguma das chaves `min_salary` ou `max_salary` estão *ausentes* no dicionário;
  - alguma das chaves `min_salary` ou `max_salary` tem valores não-numéricos;
  - o valor de `min_salary` é maior que o valor de `max_salary`;
  - o parâmetro `salary` tem valores não numéricos;
- O método  deve retornar `True` se o salário procurado estiver dentro da faixa salarial ou `False` se não estiver.

---

# Requisitos Bônus

## 9 (`Bônus`) - Implemente o método `filter_by_salary_range`
> **Implemente em:** `src/insights/salaries.py`

Agora vamos implementar o filtro propriamente dito. Para esta filtragem, podemos usar a método implementado no requisito anterior -- tomando o cuidado de descartar os empregos que apresentarem faixas salariais inválidas.

- O método deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- O método deve receber um número ou string `salary` como segundo parâmetro.
- O método deve ignorar os empregos com valores inválidos para `min_salary` ou `max_salary`.
  - Observação: strings que representem números são valores **válidos** para `min_salary` ou `max_salary`.
- O método deve retornar uma lista com todos os empregos onde o salário `salary`. estiver entre os valores da coluna `min_salary` e `max_salary`.

## 10 (`Bônus`) - Read Brazilian File (Testes)
> **Implemente em:** `tests/brazilian/test_brazilian_jobs.py`

*ps: O funcionamento da função criada para esse teste depende da implementação do método `read` em `jobs.py`*

A empresa cliente analisa relatórios em inglês, porém agora ela quer expandir seus negócios aqui para o Brasil e deseja analisar relatórios em português também. No entanto, as chaves do `dict` que usamos pra organizar os dados **devem** continuar em inglês. Ou seja: para gerar o relatório, deveremos ler as chaves em português e traduzi-las para inglês para povoar os nossos dados.

Nossa equipe já implementou essa função, a `read_brazilian_file`, na qual adotamos a estratégia de chamar o método original `read`, que implementamos no `requisito 1`, e depois traduzimos as chaves para o inglês. Agora precisamos criar testes para ter certeza que esta tudo certo!

O nome deste teste **deve** ser `test_brazilian_jobs`, e ele deve garantir que atenda as seguintes especificações:

- **Chamar** a função `read_brazilian_file` e ela deve receber um parâmetro:
  - `path` que é uma string com o caminho do arquivo csv em português (`tests/mocks/brazilians_jobs.csv`);
  - Retorna uma lista de dicionários com as chaves em inglês
