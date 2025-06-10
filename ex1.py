cpf = input("Digite o CPF: ")
 
def validacao_cpf():
    num = list(range(1,11))
    for i in num:
        for j in cpf:
            mult = i * j
            print(mult)

    
   

def tratar_cpf(c):
    if len(c) == 11 or len(c) == 14:
        if len(c) == 14:
            cpf14 = int(c.replace('.', ''),c.replace('-', ''))  
            c = cpf14 
        elif len(c) == 11:
            cpf11 = int(c)
            c = cpf11  
        


tratar_cpf(cpf)
print(cpf)



