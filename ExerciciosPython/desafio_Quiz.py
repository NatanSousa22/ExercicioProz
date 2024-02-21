perguntas = [
        {"pergunta": "Qual é a capital do Brasil?", "resposta_correta": "Brasilia"},
        {"pergunta": "Qual é o nome da empresa de tecnologia que criou o iPhone?", "resposta_correta": "Apple"},
        {"pergunta": "Quantos planetas fazem parte do nosso sistema solar?", "resposta_correta": "8"},
        {"pergunta" : "Qual é o nome do inventor do telefone?", "resposta_correta": "Alexander Graham Bell"},
        {"pergunta" : "O vinho é feito com qual fruta?", "resposta_correta": "Uva"},
        {"pergunta" : "O pão de queijo é um prato típico de qual estado brasileiro?", "resposta_correta": "Minas Gerais"},
]

while True:
    try:
        pontuacao = 0
        print("Bem-vindo ao Jogo de Perguntas e Respostas!")
     
        for pergunta_atual in perguntas:
            print("\n" + pergunta_atual["pergunta"])
            resposta_usuario = input("Sua resposta: ")

            if resposta_usuario.lower() == pergunta_atual["resposta_correta"].lower():
                print("Correto!\n")
                pontuacao += 1
            else:
                print(f"Incorreto. A resposta correta era: {pergunta_atual['resposta_correta']}\n")

        print(f"Fim do jogo! Sua pontuação final é: {pontuacao}/{len(perguntas)}")
    except KeyboardInterrupt:
        if pontuacao > 0:
            jogar_novamente = input("Deseja jogar novamente? (s/n): ")
            if jogar_novamente.lower() != 's':
                print("Obrigado por jogar. Até a próxima!")
                break
        else:
            print("Você precisa responder pelo menos uma pergunta antes de sair.")
