lista = []

#Adicionando um item a lista APPEND
lista.append("Luís")

for item in lista:
    print(item)

#Limpando a lista CLEAR
print("Limpando a lista!")
lista.clear()

for item in lista:
    print(item)

#Copy

#Count

#Extend

#Pop

#Remove

#Sort
linguagens = ["python","js","c#"]

linguagens.sort()

print(linguagens)

#Len
#Verificar a quantidade de posições (tamanho)

numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(numeros)