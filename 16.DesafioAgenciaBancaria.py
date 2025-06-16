saldo = 0
deposito = 0
saque = 0
contaSaque = 0
extrato = ""

while(True):

    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato bancário")
    opcao = int(input("Informe a opcao desejada: "))

    if opcao == 1:
        deposito = float(input("Informe o valor do depósito: "))
        if deposito <= 0:
          print("Não foi possível realizar o depósito!")
        else:
         saldo = saldo + deposito
         print("Depósito realizado com sucesso!")
         extrato += (f"Depósito: R$  {deposito:.2f} \n")
    elif opcao == 2:
        saque = float(input("Informe o valor do saque: "))
        if saque <= saldo and contaSaque < 3 and saque < 501:
           saldo -= saldo - saque
           contaSaque = contaSaque + 1
           print("Saque realizado com sucesso!")
           extrato += (f"Saque: R$  {saque:.2f} \n")
        if saldo < saque:
           print("Saldo insuficiente!")
        if saque > 500:
           print("O valor do saque é maior que R$ 500,00")
        if contaSaque >= 3:
           print("Limite de saques excedido para o dia!")
    elif opcao == 3:
       print("=========Extrato bancário=========")
       print(extrato)
       print("==================================")
