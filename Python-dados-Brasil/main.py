from cpf import Cpf
from cnpj import Cnpj
from telefones import Telefone
from date import DatasBr
from buscaCep import BuscaEndereco

#valida CPF
cpf = Cpf(91772168815)
print(cpf)

#valida CPJ
cnpj = Cnpj(20826068000131)
print(cnpj)

#validando numeros de telefone
telefone = Telefone("557996813338")
print(telefone)

#trabalhando com datas
data = DatasBr()
print(data)

#trabalhando com CEP
cep = 49032300
Cep = BuscaEndereco(cep)
Cep.acessa_via_cep()