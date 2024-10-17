# Consulta FIPE

Este projeto foi desenvolvido para automatizar o processo de consulta de informações de caminhões através da API FIPE Parallelum. O sistema realiza múltiplas requisições para diversas URLs e salva os dados obtidos em um arquivo Excel, facilitando a análise e gestão das informações.

Na empresa em que trabalho, lidamos com uma grande quantidade de veículos e suas respectivas placas. Para automatizar o processo de consulta e obter dados relevantes de cada veículo, desenvolvi uma solução que consiste em:

Automatização no Site Busca Placas: Utilizei automação para acessar o site Busca Placas, ler as placas dos veículos da empresa e salvar as respostas obtidas em um arquivo Excel.
Manipulação dos Dados via Excel: Através de querys no Excel, separei as informações como marca, modelo e ano-combustível de cada veículo.
Geração de URLs para a API FIPE: Com base nas informações extraídas, gerei as URLs adequadas para fazer requisições à API FIPE e consultar os dados detalhados de cada caminhão.

FUNCIONALIDADES PRINCIPAIS

1. Requisições Automáticas à API FIPE
O sistema realiza requisições automáticas para a API FIPE a partir de uma lista de URLs geradas com base nas informações dos veículos (marca, modelo, ano e combustível).

2. Backoff Exponencial com Re-tentativas
Para evitar bloqueios por limite de requisições, o sistema implementa um mecanismo de re-tentativa com backoff exponencial. Quando o limite de taxa é excedido, o sistema espera um tempo antes de tentar novamente.

3. Exportação para Excel
Os dados obtidos pela API FIPE são organizados e exportados para um arquivo Excel. Isso permite uma fácil análise e armazenamento das informações de todos os caminhões.

TECNOLOGIAS UTILIZADAS

1. Python: Linguagem principal utilizada para automação e manipulação de dados.

2. Requests: Utilizado para fazer requisições HTTP à API FIPE.

3. Pandas: Biblioteca utilizada para manipulação de dados e exportação para Excel.

4. Excel: Utilizado para armazenar as informações extraídas e organizadas dos veículos.


CONCLUSÃO

Este projeto oferece uma solução eficiente para consultar dados de veículos na API FIPE em larga escala, automatizando o processo de requisição e exportação dos dados para Excel. Com a implementação de re-tentativas automáticas e backoff exponencial, o sistema garante uma execução robusta e confiável, mesmo em cenários de alta carga de requisições.
