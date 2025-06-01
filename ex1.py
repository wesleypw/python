cpf = input("Digite o CPF: ")

def validacao_cpf():
    tratar = tratar_cpf(cpf)
    tratar = cpf 

    num = list(range(1,11))
    for i in num:
        for j in tratar:
            mult = i * j
            print(mult)    

def tratar_cpf(cpf):
    if len(cpf) == 11 or len(cpf) == 14:
        if len(cpf) == 14:
            cpf14 = int(cpf.replace('.', '').replace('-', ''))    
        elif len(cpf) == 11:
            cpf11 = int(cpf)
            cpf = cpf11, cpf14
        

validacao_cpf()

    

        
    
    
 



