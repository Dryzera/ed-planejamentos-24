from abc import abstractmethod, ABC
from calcs import Calculadora, Logaritmo, EquacaoSegundoGrau

class CalculadoraFactory:
    @staticmethod
    def get_operacao(tipo):
        if tipo == "logaritmo":
            return Logaritmo()
        elif tipo == "equacao_segundo_grau":
            return EquacaoSegundoGrau()
        else:
            raise ValueError("Operação desconhecida")

# Uso
operacao = CalculadoraFactory.get_operacao("logaritmo")
calculadora = Calculadora(operacao)
print(calculadora.calcular('x-2', 2))
