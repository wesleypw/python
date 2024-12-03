import random

def dados():
    valores = []
    for i in range(5):
        valores.append(random.randint(1,6))
    return valores[0], valores[1], valores[2], valores[3], valores[4]

dado1, dado2, dado3, dado4, dado5 = dados()

def jogar():
    tentativas = 3
    for i in range(tentativas):
        print(f"\n=== Tentativa {i + 1} de {tentativas} ===")
        global dado1, dado2, dado3, dado4, dado5
        dado1, dado2, dado3, dado4, dado5 = dados()
        
        dados_guardados = escolhas()
        
        # Verifica se todos os dados são iguais
        if len(dados_guardados) >= 2 an all(dado == dados_guardados[0] for dado in dados_guardados):
            print("\nParabéns! Você conseguiu dados iguais!")
            return True
        else:
            if i < tentativas - 1:  # Se não for a última                  
                print("\nTente novamente! Os dados não são iguais.")
            else:
                print("\nGame Over! Suas tentativas acabaram.")
                return False



def escolhas():
    dados_escolhidos = []
    print(f"\nDados atuais: {dado1}, {dado2}, {dado3}, {dado4}, {dado5}")
    
    for tentativa in range(3):
        print(f"\nTentativa {tentativa + 1} de 3")
        print("Quais dados você quer guardar? (Digite os números dos dados separados por espaço)")
        print("Exemplo: Se quiser guardar o primeiro e terceiro dado, digite: 1 3")
        print("Pressione Enter para pular a tentativa")
        
        escolha = input("Sua escolha: ").strip()
        
        if not escolha:  # Se o usuário só apertar Enter
            continue
            
        posicoes = escolha.split()
        for pos in posicoes:
            try:
                pos = int(pos)
                if 1 <= pos <= 5:
                    if pos == 1:
                        dados_escolhidos.append(dado)
                    elif pos == 2:
                        dados_escolhidos.append(dado2)
                    elif pos == 3:
                        dados_escolhidos.append(dado3)
                    elif pos == 4:
                        dados_escolhidos.append(dado4)
                    elif pos == 5:
                        dados_escolhidos.append(dado5)
                else:
                    print(f"Posição {pos} inválida. Use números de 1 até 5.")
            except ValueError:
                print(f"Entrada inválida: {pos}. Por favor, digite apenas números de 1 até 5.")
                
        print(f"Dados guardados até agora: {dados_escolhidos}")
    
def menu():
    print("=== MENU ===")
    print("Esse é o jogo do general")
    print("vamos comecar?")
    print("digite 1 para sim")
    print("digite 2 para nao")
    while True:
        opcao = int(input("digite a opcao desejada: "))
        if opcao == 1:
            jogar()
        elif opcao == 2:
            print("obrigado por jogar")
            break
        else:
            print("opcao invalida")
