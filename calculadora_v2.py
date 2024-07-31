saida = ''

def adicao(num1, num2):
    return num1 + num2

def subracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao == 'adição':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtração':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicação':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisão':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    
    return resultado

while saida.lower() != 'n':

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou nome da operação): ").lower()
    
    resultado = calculadora(numero1, numero2, operacao)
    print(f'Resultado da operação: {resultado}')
    
    saida = input("Deseja continuar? (S/N): ").lower()

print("Programa encerrado.")