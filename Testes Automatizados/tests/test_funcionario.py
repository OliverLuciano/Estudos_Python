from codigo.funcionario import Funcionario

class Test_Class:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2001'
        esperado = 22
        
        Funcionario_Teste = Funcionario('Teste',entrada, 11111)
        resultado = Funcionario_Teste.idade()
        
        assert resultado == esperado
        
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_carvalho(self):
        entrada = "Lucas Carvalho"
        esperado = "Carvalho"
        
        lucas = Funcionario(entrada, "11/02/2001", 10000)
        resultado = lucas.sobrenome()
        
        assert resultado == esperado