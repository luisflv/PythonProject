#Desvio de fluxo quando determinadas expressões lógicas são atendidas
#if / if else / elif

#if simples
idade  = 18

if idade >= 18:
    print("Maior de idade!")


#if else

#elif




#If aninhado - If dentro de if

conta_normal = False
conta_universitaria = True

saldo = 200
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque > saldo:
        print("Não foi possível!")

#If ternario

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")