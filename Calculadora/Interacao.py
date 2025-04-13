from .calcular import Calcular

class IniciarCalculadora:
    def __init__(self):
        self.operacoes = {
            '1': 'somar',
            '2': 'subtrair',
            '3': 'multiplicar',
            '4': 'dividir'
        }

    def start(self):
        print('Bem-vindo à Calculadora!')

        while True:
            try:
                print('\nSelecione uma operação: ')
                print('1 - Soma')
                print('2 - Subtração')   
                print('3 - Multiplicação')
                print('4 - Divisão')
                print('5 - Sair')

                escolha = input('Escolha uma opção: ')

                if escolha == '5':
                    print('Saindo...')
                    break

                if escolha not in self.operacoes:
                    print('Opção Inválida! Tente novamente.')
                    continue

                operacao = self.operacoes[escolha]
                
                while True:
                    try:
                        x = float(input('Digite o primeiro número: '))
                        y = float(input('Digite o segundo número: '))
                        break  
                    except ValueError:
                        print("Entrada inválida! Por favor, digite um número válido.")

                calculadora = Calcular()
                resultado   = calculadora.calcular(operacao, x, y)

                print(f'O Resultado é: {resultado}')
                
            except ValueError as e:
                print(f"Erro: {e}")

            except KeyboardInterrupt:
                print("\nCalculadora finalizada. Até mais!")
                break

            except Exception as e:
                print(f"Ocorreu um erro: {e}")