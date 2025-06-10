def valida_cpf_cnpj(valor: str) -> bool:
    """
    Valida um CPF (11 dígitos) ou CNPJ (14 dígitos).
    Aceita formatos com ou sem máscara.
    Retorna True se for válido, False caso contrário.
    """
    # Função interna para validar CPF
    def valida_cpf(cpf: str) -> bool:
        # Verifica se o tamanho é 11
        if len(cpf) != 11:
            return False
        # Verifica se todos os dígitos são iguais (ex: 11111111111)
        if cpf == cpf[0] * 11:
            return False
        # Calcula o primeiro dígito verificador do CPF
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10
        # Calcula o segundo dígito verificador do CPF
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10
        # Verifica se os dígitos calculados conferem com os informados
        return cpf[-2:] == f"{digito1}{digito2}"

    # Função interna para validar CNPJ
    def valida_cnpj(cnpj: str) -> bool:
        # Verifica se o tamanho é 14
        if len(cnpj) != 14:
            return False
        # Verifica se todos os dígitos são iguais (ex: 11111111111111)
        if cnpj == cnpj[0] * 14:
            return False
        # Primeiro dígito verificador do CNPJ
        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        # Segundo dígito verificador do CNPJ
        pesos2 = [6] + pesos1
        soma = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        # Verifica se os dígitos calculados conferem com os informados
        return cnpj[-2:] == f"{digito1}{digito2}"

    # Remove todos os caracteres que não são números
    numero = ''.join(filter(str.isdigit, valor))
    # Se tiver 11 dígitos, tenta validar como CPF
    if len(numero) == 11:
        return valida_cpf(numero)
    # Se tiver 14 dígitos, tenta validar como CNPJ
    elif len(numero) == 14:
        return valida_cnpj(numero)
    # Qualquer outro tamanho é inválido
    else:
        return False


if __name__ == "__main__":
    # Lista de exemplos para testar as validações
    exemplos = [
        "529.982.247-25",   # CPF válido
        "123.456.789-09",   # CPF inválido
        "111.111.111-11",   # CPF inválido
        "39053344705",      # CPF válido
        "04.252.011/0001-10", # CNPJ válido
        "11.222.333/0001-81", # CNPJ inválido
        "04252011000110",     # CNPJ válido
        "11222333000181",     # CNPJ inválido
        "1234567890",         # inválido (tamanho)
    ]
    # Para cada exemplo, imprime se é válido ou inválido
    for doc in exemplos:
        print(f"{doc}: {'Válido' if valida_cpf_cnpj(doc) else 'Inválido'}")

