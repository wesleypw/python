import random

amigo_secreto =  {}
numero_amigo_secreto = 0
def sortear_amigo_secreto():
    amigo = input("Digite o nome do amigo: ")
    if amigo.lower() == "sair":
        print("Obrigado por jogar!")
        return
    for amigo, amigo_secreto in amigo_secreto.items():
         print(f"Amigo: {amigo} - Amigo Secreto: {amigo_secreto}")
    

def menu():
    print("="*20)
    print("======= MENU =======")
    print("="*20)
    print("Digite o nome dos participantes ou \"sair\" para sair")
    sortear_amigo_secreto()

menu()