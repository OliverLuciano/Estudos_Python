class EXTRATOR_URL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        return url.strip()
    
    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL ESTÁ VAZIA")
        
    def get_url_base(self):
        dados = self.split("?")
        url_base = dados[0]
        return url_base

    def get_url_parametros(self):
        dados = self.url.split("?")
        url_parametros = dados[1]
        return url_parametros
        
    def get_valor_parametro(self):
        dados = []
        parametros = self.get_url_parametros()
        parametros = parametros.split("&")
        for parametro in parametros:
            dado_index = parametro.find('=')
            dado_valor = parametro[dado_index + 1 :]
            dados.append(dado_valor)
        return dados




extrator_url = EXTRATOR_URL( "https://bytebank.com/cambio?moedaOritem=real&moedaDestino=dolar")
parametros = extrator_url.get_valor_parametro()
print(parametros)