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
        
    def test_quando_recebe_10000_retorna_1000_na_hora_do_bonus(self):
        entrada = 10000
        esperado = 1000
        
        funcionario = Funcionario("teste","11/02/2000",entrada)
        resultado = funcionario.calcular_bonus()
        
        assert resultado == esperado