import random

cartas = {'1ª Carta': 'O Passado: Representa a lição que acabou de ser aprendida.',
'2ª Carta': 'A Porta da Tenda (Presente): Simboliza a lição que está sendo aprendida no momento presente.',
'3ª Carta': 'O Futuro: Revela como as ações e aprendizados do presente influenciam o futuro.',
'4ª Carta': 'O Mastro Central: Representa a estrutura que sustenta a tenda, ou seja, a base necessária para manter as atividades em andamento.',
'5ª Carta': 'A Proteção da Tenda: Simboliza a proteção espiritual e a magia pessoal do indivíduo, revelando as forças que podem ser invocadas para auxílio e cura.',
'6ª Carta': 'A Abertura da Fumaça: Representa o topo da tenda, por onde a fumaça da fogueira se eleva ao Pai Céu. Simboliza a realização de necessidades e o atendimento de preces.',
'7ª Carta': 'A Ponta Solta da Corda: Simboliza um desafio inesperado. A corda solta da tenda permite a entrada de elementos externos, como neve, chuva e vento, representando as dificuldades que podem surgir.',
'8ª Carta': 'A Bandeira da Vitória: Representa as tiras no topo dos mastros da tenda, simbolizando a vitória e a capacidade adquirida através da superação dos desafios.'}

cartas_escolhidas = []


def menu():
 print("=== MENU ===")
 print("digite 1 para tirar uma carta")
 print("digite 2 para sair")
 while True:
    opcao = int(input("digite a opcao desejada: "))
    if opcao == 1:
        jogar()
    elif opcao == 2:
        print("obrigado por jogar")
        break
    else:
        print("opcao invalida")


def jogar():
  
 carta = random.choice(list(cartas.items()))
 cartas_escolhidas.append(carta)
 if cartas_escolhidas == cartas:
    print("Parabéns, você acabou de descobrir todas as cartas!")
    return menu()   
 print(f"carta sorteada: {carta}")
menu()
            



         






    
    













    
    
    
    
    
    




