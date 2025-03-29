from abc import ABC, abstractmethod
import math
from os import name

# Interface de Estratégia
class OperacaoCalculadora(ABC):
    @abstractmethod
    def calcular(self, *args):
        pass

# Estratégia de Logaritmo
class Logaritmo(OperacaoCalculadora):
    def calcular(self, numero, base):
        return round(math.log(numero, base), 2)

# Estratégia de Equação de Segundo Grau
class EquacaoSegundoGrau(OperacaoCalculadora):
    def calcular(self, a, b, c):
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            return "Sem soluções reais"
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return (x1, x2)

# Contexto (Calculadora)
class Calculadora:
    def __init__(self, operacao: OperacaoCalculadora):
        self.operacao = operacao
    
    def set_operacao(self, operacao: OperacaoCalculadora):
        self.operacao = operacao
    
    def calcular(self, *args):
        return self.operacao.calcular(*args)

if name == '__main__':
    # Uso
    calculadora = Calculadora(Logaritmo())
    print(calculadora.calcular(100000, 3))  # Exemplo de logaritmo

    calculadora.set_operacao(EquacaoSegundoGrau())
    print(calculadora.calcular(1, -3, 2))  # Exemplo de equação quadrática
