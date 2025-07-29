def mensagemUm():
    print("Hello world!")

def mensagemDois(nome):
    print(f"Olá, {nome}")

def mensagemTres(nome="Anônimo"):
    print(f"Seja bem-vindo: {nome}")

#Chamando as funções

mensagemUm()

mensagemDois("Luís")

mensagemTres() #Não passando argumento
mensagemTres() #Passando argumento

#Criando um função para calcular a soma de uma lista de valores

listaNumeros = [2,4,8,16]

def somaValores(valor):
    return sum(valor)

resultado = somaValores(listaNumeros)

print(resultado)

#Criando uma função para retornar o antecessor e o sucessor de um valor

def antecessorSucessor(valor):
    antecessor = valor - 1;
    sucessor = valor + 1
    return antecessor,sucessor

print(antecessorSucessor(10))


#Função com argumentos nomeados

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro cadastrado com sucesso {marca} | {modelo} | {ano} | {placa}")

salvar_carro(marca="Fiat",modelo="Uno",ano=2005,placa="ABC-1234")