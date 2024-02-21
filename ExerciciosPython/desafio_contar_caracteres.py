def contar_caracteres (texto):
    return len(texto)

def contar_palavras(texto):
    palavras = texto
    return len(palavras)
while True:
    print("Escolha uma opção: ")
    print("1. Contar caracteres")
    print("2. Contar palavras")
    print("3. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "3":
        print("Saindo do programa.")
        break
    elif escolha in ["1", "2"]:
        entrada_texto = input("Digite o texto: ")
        if escolha == "1":
            resultado = contar_caracteres(entrada_texto)
            print(f"O texto tem {resultado} caracteres.")
        elif escolha == "2":
            resultado = contar_palavras(entrada_texto)
            print(f"O texto tem {resultado} palavras.")
    else:
        print("Erro. Tente novamente")
        
