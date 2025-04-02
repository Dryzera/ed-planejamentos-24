from abc import ABC, abstractmethod
import math

class OperacaoCalculadora(ABC):
    @abstractmethod
    def calcular(self, *args):
        pass

class Logaritmo(OperacaoCalculadora):
    def calcular(self, numero, base):
        return round(math.log(numero, base), 2)

class EquacaoSegundoGrau(OperacaoCalculadora):
    def calcular(self, a, b, c):
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            return "Sem soluções reais"
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return (x1, x2)
    
class EquacaoPrimeiroGrau(OperacaoCalculadora):
    def calcular(self, valor_x, valores):
        return valores / valor_x

class Calculadora:
    def __init__(self, operacao: OperacaoCalculadora):
        self.operacao = operacao
    
    def set_operacao(self, operacao: OperacaoCalculadora):
        self.operacao = operacao
    
    def calcular(self, *args):
        return self.operacao.calcular(*args)

if __name__ == '__main__':
    calculadora = Calculadora(Logaritmo())
    print(calculadora.calcular(100000, 3))

    calculadora.set_operacao(EquacaoSegundoGrau())
    print(calculadora.calcular(1, -3, 2))

    calculadora.set_operacao(EquacaoPrimeiroGrau())
    print(calculadora.calcular(8, 2))
