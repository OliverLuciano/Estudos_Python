import re

class EXTRATOR_URL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL ESTÁ VAZIA")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL é invalida!")
        
        
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




extrator_url = EXTRATOR_URL( "https://bytebank.com/cambio?moedaOritem=real&moedaDestino=dolar&quantidade=100")
parametros = extrator_url.get_valor_parametro()
print(parametros)