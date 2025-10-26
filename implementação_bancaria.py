menu = """

[s] Sacar
[d] Depositar
[e] Extrato
[c] Criar conta
[q] Sair

=> """
dados_usuario = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def saque(*, saldo, limite, extrato, numero_saques):
       
    valor = float(input("Informe o valor do saque: "))

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedide.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

        print(f"Sucesso! Você realizou o saque no valor de R$ {valor:.2f}\n")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def deposito(saldo, extrato, /):

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Sucesso! Você realizou o depósito no valor de R$ {valor:.2f}\n")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo,/, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(dados_usuarios):
    cpf = input("Por gentileza, informe o seu CPF: ")


    for usuario in dados_usuarios:
        if cpf == usuario["cpf"]:
            print("Já existe um usuário utilizando este CPF")
            return dados_usuarios
        
    nome = input("Por gentileza, informe o seu nome completo: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    rua = input("Informe sua rua/logradouro: ")
    numero = input("Número de rêsidencia: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("Sigla de seu estado: ")
    dados_usuarios.append({"nome": nome.title(), "nascimento": data_nascimento, "cpf": cpf, "endereço": f"{rua.title()}, {numero} - {bairro.title()} - {cidade}/{uf.upper()}"})

    print(dados_usuarios)
    return dados_usuarios

while True:

    opcao = input(menu)

    if opcao == "s":
        saldo, extrato, numero_saques = saque(saldo = saldo, limite = limite, extrato = extrato, numero_saques= numero_saques)
    

    elif opcao == "d":
       saldo, extrato = deposito(saldo, extrato)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        dados_usuario = cadastrar_usuario(dados_usuario)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
