# ValidadorDeInfos
 
Este é um script em Python que valida as informações contidas em um arquivo de texto em relação a um conjunto de informações esperadas.

1. **Definição do arquivo e das informações esperadas**:
   - `arquivoTxt`: Caminho para o arquivo de texto que contém as informações a serem validadas.
   - `infosEsperadas`: Um dicionário contendo as informações esperadas, onde as chaves são os nomes dos campos e os valores são os valores esperados para cada campo.

2. **Função `Validador`**:
   - Recebe dois argumentos: `dados`, que é o arquivo de texto aberto para leitura, e `infosEsperadas`, que é o dicionário com as informações esperadas.
   - Itera sobre cada linha do arquivo de texto.
   - Para cada linha, divide a linha em chave e valor usando `split(':')`, removendo espaços em branco com `strip()`.
   - Verifica se a chave está presente nas informações esperadas. Se não estiver, imprime um erro indicando que a chave não é esperada.
   - Se a chave estiver presente nas informações esperadas, verifica se o valor corresponde ao valor esperado. Se corresponder, imprime uma mensagem de validação bem-sucedida. Se não corresponder, imprime um erro indicando o valor incorreto.
   - Se ocorrer um erro durante a leitura ou validação do arquivo, imprime uma mensagem de erro.

3. **Bloco `try-except` principal**:
   - Abre o arquivo de texto especificado em modo de leitura.
   - Chama a função `Validador` passando o arquivo aberto e as informações esperadas como argumentos.
   - Se o arquivo especificado não for encontrado, imprime uma mensagem de erro indicando que o arquivo não foi encontrado.

Este script é útil para validar informações em um arquivo de texto em relação a um conjunto de informações esperadas e identificar quaisquer desvios ou inconsistências entre os valores esperados e os valores encontrados no arquivo.
