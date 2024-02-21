#Definir a função 
def calcular():
    operação = input ('''Por favor, Type in operação matemática que você gostaria de concluir:

+ for Adição
- for Subtração
* for Multiplicação
/ for Divisão
''')

    numero_1 = int(input("Digite o primeiro número "))
    numero_2 = int(input("Digite o segundo número "))



#Adição
    if operação == "+":
     print('{} + {}'.format(numero_1, numero_2))
     print(numero_1 + numero_2)

#Subtração
    elif operação == "-":
     print('{} - {}'.format(numero_1, numero_2))
     print(numero_1 - numero_2)

#Multiplicação
    elif operação == "*":
     print('{} * {}'.format(numero_1, numero_2))
     print(numero_1 * numero_2)

#Divisão
    elif operação == "/":
     print('{} / {}'.format(numero_1, numero_2))
     print(numero_1 / numero_2)

    else:
     print("Digite um número válido.")

#Chamar calcular() fora da função
    novamente()

#Defina a função novamente() para perguntar ao usúario se ele deseja usar a calculadora novamente. 
def novamente():
     # Receba informações do usúario
    calcule_novamente = input(''' Deseja calcular novamente? Type S for Sim or N for Não.'''  )


     # Se o usúario digitar S, execute a função calcular
    if calcule_novamente.upper() == "S":
          calcular()
     # Se o usúario digitar N, Encerre o programa
    elif calcule_novamente.upper() == "N":
          print("Até Breve!")
     # Se o usúario digitar outra chave, execute o código novamente
    else:
          novamente()

# Chamar calcular() fora da função
calcular()