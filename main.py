import requests
import time
import pandas as pd

urls = [
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/6706/years/2017-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5788/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/6508/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/3800/years/2006-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5853/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/6706/years/2017-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5788/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/6508/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/3800/years/2006-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5853/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/4037/years/2010-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/4038/years/2010-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5846/years/2013-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/5798/years/2016-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5850/years/2016-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/6706/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/7472/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/9504/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5850/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/7446/years/2023-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/10521/years/2024-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/10526/years/2024-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/10556/years/2024-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/10266/years/2023-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/105/models/3201/years/2010-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/6028/years/2013-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/3951/years/2007-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/105/models/3985/years/2012-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/4037/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/4038/years/2008-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/6028/years/2012-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/3951/years/2008-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/4037/years/2006-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/4038/years/2007-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3429/years/2004-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/105/models/6980/years/2016-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/5809/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5788/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/7414/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/7655/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5786/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5788/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/7655/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5777/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5850/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/8196/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/8196/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5795/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5788/years/2017-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/8609/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/188/models/9729/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/188/models/6315/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/8609/years/2023-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/7414/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/4180/years/2012-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/5809/years/2012-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/105/models/3242/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/4212/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/105/models/5568/years/2012-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3429/years/2007-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3351/years/2006-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/4219/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/6257/years/2016-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/5945/years/2016-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/7655/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/7683/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3351/years/2009-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3351/years/2010-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3351/years/2008-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5866/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/10500/years/2023-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/5819/years/2013-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5777/years/2016-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/6007/years/2015-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/4232/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3429/years/2006-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/105/models/3210/years/2009-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/6706/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5777/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/7389/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/5798/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/10236/years/2024-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/105/models/3198/years/2009-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/105/models/3181/years/2010-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3365/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/4212/years/2010-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3369/years/2006-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/105/models/3198/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/5798/years/2015-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5853/years/2016-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5770/years/2013-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/8733/years/2023-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3308/years/1997-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/3649/years/2002-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3403/years/2006-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/4219/years/2010-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5850/years/2017-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/7414/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/5809/years/2015-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5786/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/8733/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/8626/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5835/years/2014-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/8609/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5850/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5853/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5837/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/3682/years/1998-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/3730/years/2001-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/105/models/3157/years/1998-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3328/years/2000-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3409/years/2000-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/3457/years/1996-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/6257/years/2015-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/7301/years/2015-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/6864/years/2014-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/5954/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/7446/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/8761/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5846/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5786/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5866/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5864/years/2015-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5866/years/2015-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/8623/years/2023-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5853/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/4213/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5786/years/2016-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/6478/years/2016-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/6257/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/6864/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/6864/years/2015-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/5948/years/2015-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/7683/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/5954/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/9504/years/2021-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/10117/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/4239/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/10526/years/2023-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5850/years/2015-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5850/years/2018-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5850/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/3741/years/2000-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5786/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/3945/years/2008-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5853/years/2013-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/5334/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5853/years/2017-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/184/models/6457/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5853/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/8682/years/2023-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5777/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5792/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5777/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/7446/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/8733/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/5954/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/109/models/5764/years/2019-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/3945/years/2009-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/3704/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/3945/years/2010-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/3945/years/2011-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/10302/years/2023-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/5957/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/5954/years/2023-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/6684/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/115/models/9246/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5865/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/8312/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/197/models/6706/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/122/models/8682/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/114/models/8683/years/2022-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/184/models/7369/years/2020-3",
    "https://fipe.parallelum.com.br/api/v2/trucks/brands/116/models/5864/years/2020-3",

]

# Cabeçalhos da requisição (com token de autenticação)
cabecalhos = {
    "Authorization": "SEU TOKEN"
}

### função para tentar realizar a requisição com retries e backoff exponencial ###
def obter_dados_com_retry(url, cabecalhos, tentativas=5, fator_backoff=1):
    for i in range(tentativas):
        resposta = requests.get(url, headers=cabecalhos)
        ### se a resposta for 200, retorna os dados no formato json ###
        if resposta.status_code == 200:
            return resposta.json()
        ### se a resposta for 429, aplica o backoff exponencial ###
        elif resposta.status_code == 429:
            espera = fator_backoff * (2 ** i)
            tempo_reset = resposta.headers.get("Retry-After")
            if tempo_reset:
                espera = int(tempo_reset)
            print(f"Limite de taxa excedido. Aguardando {espera} segundos...")
            time.sleep(espera)
        ### caso haja erro, exibe a mensagem e levanta a exceção ###
        else:
            print(f"Erro para {url}: {resposta.status_code}")
            resposta.raise_for_status()
    ### se todas as tentativas falharem, lança uma exceção ###
    raise Exception("Máximo de tentativas excedido")

### função para buscar dados de todas as URLs ###
def buscar_todos_dados(urls, cabecalhos):
    todos_dados = []
    for url in urls:
        try:
            print(f"Buscando dados para {url}")
            dados = obter_dados_com_retry(url, cabecalhos)
            todos_dados.append(dados)
        ### trata erros durante a busca de dados ###
        except Exception as e:
            print(f"Falha ao buscar dados para {url}: {e}")
    return todos_dados

### função para salvar os dados em um arquivo Excel ###
def salvar_em_excel(lista_dados, nome_arquivo):
    ### achata os dados JSON em uma lista de dicionários ###
    dados_achatados = []
    for dados in lista_dados:
        if isinstance(dados, dict):
            dados_achatados.append(dados)
        elif isinstance(dados, list):
            dados_achatados.extend(dados)

    ### cria um DataFrame e exporta para Excel ###
    df = pd.DataFrame(dados_achatados)
    df.to_excel(nome_arquivo, index=False)

### executando o processo de busca e salvamento ###
try:
    todas_informacoes_caminhoes = buscar_todos_dados(urls, cabecalhos)
    salvar_em_excel(todas_informacoes_caminhoes, "FIPE_01_10_2024.xlsx")
    print("Dados exportados para FIPE_01_10_2024.xlsx")
except Exception as e:
    print(f"Erro: {e}")
