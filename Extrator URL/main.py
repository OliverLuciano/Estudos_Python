def filtra_valor (dado):
    dado_index = dado.find('=')
    dado_valor = dado[dado_index + 1 :]
    return dado_valor

url = "https://bytebank.com/cambio?moedaOritem=real&moedaDestino=dolar"
url = ""

#Sanitização da URL
url = url.strip()

#validação da URL
if url == "":
    raise ValueError("A URL ESTÁ VAZIA")

#Separa a base dos parametros
dados = url.split("?")
url_base = dados[0]
url_parametros = dados[1]

#Filtra os valores dos parametros 
parametros = url_parametros.split("&")
primeiro_parametro = parametros[0]
primeiro_parametro_valor = filtra_valor(primeiro_parametro)

segundo_parametro = parametros[1]
segundo_parametro_valor = filtra_valor(segundo_parametro)

print(url)
print(url_base)
print(f"primeiro parametro tem o valor de {primeiro_parametro_valor} e o segundo parametro tem o valor de {segundo_parametro_valor}")
