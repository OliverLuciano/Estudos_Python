from codigo.funcionario import Funcionario

class Test_Class:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given-contexto
        entrada = '13/03/2001'
        esperado = 22
        
        Funcionario_Teste = Funcionario('Teste',entrada, 11111)
        resultado = Funcionario_Teste.idade()
        
        assert resultado == esperado