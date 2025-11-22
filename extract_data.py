import pandas as pd

participantes_enem = 'PARTICIPANTES_2024.csv'

#Como o arquivo é muito grande, resolvi selecionar apenas algumas colunas
colunas_analisadas = [
    'NU_INSCRICAO', 
    'NU_ANO', 
    'SG_UF_PROVA', 
    'TP_SEXO',

]

try:
    df = pd.read_csv(
        participantes_enem, 
        encoding='latin-1', 
        sep=';', 
        usecols=colunas_analisadas 
    )
    
    print("Arquivo carregado com sucesso!")
    print("\n Informações da Estrutura")
    df.info()

    print("\n Primeiras 5 linhas da tabela")
    print(df.head())

    print("\n 5 Últimas linhas da tabela")
    print(df.tail())

    print('\n Lista de candidatos que fizeram a prova no RS')
    candidatos_rs = df[df['SG_UF_PROVA'] == 'RS']
    print(candidatos_rs)
    print(f'\nTotal de candidatos no RS: {candidatos_rs.shape[0]}')
    
except Exception as e:
    print(f"\nErro ao carregar o arquivo: {e}")