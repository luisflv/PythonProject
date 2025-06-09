#while com break
print("While com break")

while True:
    valor = int(input("Informe o valor: "))
    if valor == 10:
        break
    
    print(f"{valor} digitado!")

#while

contador = 1

while (contador <= 10):
    print(contador)
    contador = contador + 1

#for
#utilizando um iterável

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")


#Exemplo utilizando a função built-in range

list(range(4))

for numero in range(0,11):
    print(numero, end=" ")

print()

#Exibindo a tabuada do 5
for numero in range(0,51,5):
    print(numero, end=" | ")