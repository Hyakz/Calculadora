class Operacoes:
    def __init__(self, x: float, y: float):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Os valores devem ser numéricos (int ou float).')
        
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