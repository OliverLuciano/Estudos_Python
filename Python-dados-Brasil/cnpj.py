from validate_docbr import CNPJ

class Cnpj:
    def __init__(self,documento):
        documento = str(documento)
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")
            
    def __str__(self):
        return self.formata_cnpj()
        
        
    def valida_cnpj(self,documento):
        if len(documento) == 14:
            cnpj = CNPJ()
            return cnpj.validate(documento)
        else:
            raise ValueError("CNPJ inválido!")
        
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
        