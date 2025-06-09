#Conversão de Inteiro para float
preco = 10
print(preco)

preco = float(preco)
print(preco)

#Conversão de Float para inteiro
preco = 10.45
print(preco)

preco = int(preco)
print(preco)

#Conversão por divisão
preco = 10
print(preco)
#Utilizando / ele preserva o valor decimal
print(preco / 2)
#Utilizando // ele preserva apenas o valor inteiro
print(preco // 2)

#Numérico para string
preco = 10.50
idade = 28

print(str(preco))
print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)


#String para número
preco = "10.50"
idade = "28"

print(float(preco))
print(int(idade))

#Erro de conversão

#preco = "python"
print(float(preco))

#Verificando tipos de dados

valor = 10
valor_str = "10"
valor_str = 'a'
valor_float = 10.25
valor_logico = True

print(type(valor))
print(type(valor_str))
print(type(valor_char))
print(type(valor_float))
print(type(valor_logico))
