from .operacoes import Operacoes

class Calcular:
    def __init__(self):
        self.resultado = 0

    def calcular(self, operacao, x, y):
        op = Operacoes(x, y)

        operacoes = {
            'somar'       : op.somar,
            'subtrair'    : op.subtrair,
            'multiplicar' : op.multiplicar,
            'dividir'     : op.dividir
        }

        if (operacao in operacoes):
            self.resultado = operacoes[operacao]() 
        else:
            raise ValueError('Operação inválida!')
        
        return self.resultado