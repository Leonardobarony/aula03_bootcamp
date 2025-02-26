nome_valido = False
salario_valido = False
bonus_valido = False


while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        nome_list = list(nome)
        validar_nome = [char.isdigit() for char in nome_list]
        soma_nome = sum(validar_nome)
        if soma_nome > 0:
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)
