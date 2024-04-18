arquivoTxt = 'F:\Repo_GitHub\Codes_in_Py\ValidadosDeInfos\infos.txt'
infosEsperadas = {
    'Nome': 'Joao da Silva',
    'Idade': '25',
    'Cidade': 'Sao Paulo',
}

def Validador(dados, infosEsperadas):
    try:
        linhas = dados.readlines()
        for linha in linhas:
            chave, valor = linha.strip().split(':')
            print(f'{infosEsperadas[chave]}')
            
            if chave in infosEsperadas:
                if infosEsperadas[chave] == valor.strip():
                    print(f"Validação bem-sucedida para {chave}: {valor}")
                else:
                    print(f'Erro: Valor incorreto para {chave}. Esperado: {infosEsperadas[chave]}, Obtido: {valor}')
            else:
                print(f'Erro: Chave {chave} não esperada.')
    except ValueError as e:
        print(f'Erro durante a leitura ou validação do arquivo: {type(e).__name__}')
                    

try:
    with open(arquivoTxt, 'r', encoding='utf-8') as dados:
        Validador(dados, infosEsperadas)
except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivoTxt}' não encontrado.")
    
