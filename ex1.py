cpf = input("Digite o CPF: ")

while True:
    if len(cpf) == 11 or len(cpf) == 14:
        if len(cpf) == 14:
            cpf = cpf.replace(".", "-")
            print(cpf)
            break
           
    else:
        print("CPF inválido")
        break


    

        
    
    
 



