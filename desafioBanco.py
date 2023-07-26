# 3 saque diárioos com limite máximo de 500 por saque
# caso n tenha saldo suficiente exibir mensagem
#todos os saques devem ser exibidos no extrato

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0
limite = 500 
extrato = "" 
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Valor a ser depositado: "))
        saldo+= deposito
        print(f"Deposito no valor de R${deposito:.2f} feito com sucesso.")
        extrato += f"Deposito: R$ {deposito:.2f}\n"
        
    elif opcao == "s":

        while numero_saques < LIMITE_SAQUES and saldo > 0:
            sacar = float(input("Valor a ser sacado: "))
            if sacar > limite:
                print("Limite máximo de saque atingido")
            elif sacar > limite and sacar > saldo:
                print("Você não tem saldo suficiente para sacar e excede o limite de saque: ")
            else:
                saldo -= sacar
                print(f"Saque no valor de R${sacar:.2f} feito com sucesso.")
                print(f"Seu saldo após o saque é de R${saldo:.2f}.")
                extrato += f"Saque: R$ {sacar:.2f}\n"
                numero_saques += 1
                break
    
    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações.")
            print(f"Saldo: R$ {saldo:.2f}")
        else:
            print(extrato)
            print(f"Numero de saques efetudados: {numero_saques}")
            print(f"Saldo disponível: R$ {saldo}.")

    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")