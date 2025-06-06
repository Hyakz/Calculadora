class Operacoes:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def somar(self) -> float:
        return self.x + self.y
    
    def subtrair(self) -> float:
        return self.x - self.y
    
    def multiplicar(self) -> float:
        return self.x * self.y
    
    def dividir(self) -> float:
        if(self.y == 0):
            raise ValueError('Divisão por zero!')
        return self.x / self.y