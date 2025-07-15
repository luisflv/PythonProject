
#Criando uma lista para armazenar nomes de frutas

frutas = ["maçã", "laranja", "uva"]

print(frutas[0])

print(frutas[-1])

#Criando uma lista para guardar valores de 0 a 9

numeros = list(range(10))

for num in numeros:
    print(num)


#Matriz em python

matriz = [
    [1, "a", "amarelo"],
    [2, "v", "vermelho"],
    [3, "r", "roxo"]
]

print(matriz[0][1])

#Funcao enumerate
#Saber o indice ENUMERATE

carros = ["Gol","Uno","HB20"]

for indice,carro in enumerate(carros):
    print(f"{indice} : {carro}")

#Compreensão de listas

numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if (numero % 2 == 0):
        pares.append(numero)

for num in pares:
    print(num)

#comprehension
print("Lista com pares comprehension: ")
pares = [numero for numero in numeros if numero % 2 == 0]

for num in pares:
    print(num)
