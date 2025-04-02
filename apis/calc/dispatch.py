from calcs import *

class CalculadoraFactory:
    @staticmethod
    def get_operacao(tipo):
        match tipo:
            case 'logaritmo':
                return Logaritmo()
            case "equacao_segundo_grau":
                return EquacaoSegundoGrau()
            case 'equacao_primeiro_grau':
                return EquacaoPrimeiroGrau()
            case _:
                raise ValueError("Operação desconhecida")

# Uso
operacao = CalculadoraFactory.get_operacao("equacao_primeiro_grau")
calculadora = Calculadora(operacao)
print(calculadora.calcular(-2,-6))