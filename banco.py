def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))  # Solicita valor do depósito
        if valor > 0:
            saldo += valor  # Adiciona ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra no extrato
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato  # Retorna saldo e extrato atualizados

def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    try:
        valor = float(input("Informe o valor do saque: "))  # Solicita valor do saque
        excedeu_saldo = valor > saldo  # Verifica se há saldo suficiente
        excedeu_limite = valor > limite  # Verifica se excede o limite por saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se excedeu o número de saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor  # Subtrai do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra no extrato
            numero_saques += 1  # Incrementa o número de saques
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato, numero_saques  # Retorna saldo, extrato e número de saques atualizados

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)  # Mostra extrato ou mensagem padrão
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()  # Solicita opção do usuário

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)  # Chama função de depósito
    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)  # Chama função de saque
    elif opcao == "e":
        exibir_extrato(saldo, extrato)  # Chama função de extrato
    elif opcao == "q":
        break  # Sai do loop e encerra o programa
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
