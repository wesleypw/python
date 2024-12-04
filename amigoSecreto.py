import random

def sortear_amigo_secreto():
    participantes = input("digite os nomes dos participantes (separadospor espaco): ").split(" ")
    return [p for p in participantes]

def realizar_sorteio(participantes):
    # Cria uma cópia da lista de participantes para não modificar a lista original
    amigos = participantes.copy()
    # Embaralha aleatoriamente a ordem dos nomes na lista amigos
    random.shuffle(amigos)
    
    # Loop que percorre cada posição da lista usando índices (0, 1, 2, etc.)
    for i in range(len(participantes)):
        # Verifica se alguém tirou o próprio nome
        # (se na mesma posição i, o nome é igual nas duas listas)
        if participantes[i] == amigos[i]:
            print(f"esse nome esta se repetindo ")
            # Se alguém tirou o próprio nome, faz um novo sorteio
            return realizar_sorteio(participantes)
    # Cria um dicionário onde:
    # - Chave: nome de quem vai dar o presente (lista participantes)
    # - Valor: nome de quem vai receber o presente (lista amigos)
    return {participantes[i]: amigos[i] for i in range(len(participantes))}

def display_results(results):
  print("\nAmigo secreto:")
  for giver, receiver in results.items():
    print(f"senhor(a) {giver} seu amigo secreto é {receiver}")

def menu():
    
    print("="*20)
    print("======= MENU =======")
    print("="*20)
    participantes = sortear_amigo_secreto()
    results = realizar_sorteio(participantes)
    display_results(results)

if __name__ == "__main__":
 menu()