#Métodos comuns
curso = "pYtHon"
print(f"Maiúsculo: {curso.upper()}")
print(f"Minúsculo: {curso.lower()}")
print(f"Primeira letra maiúscula: {curso.title()}")

#Remover espaço em branco do início e do fim
curso = "    Python  "

print(curso)

print(curso.strip() + ".")
print(curso.lstrip() + ".")
print(curso.rstrip() + ".")

#Junções e centralização
curso = "Python"

print(curso.center(10,"#"))
print(".".join(curso))

#Interpolação de variáveis
#Old Style %
nome = "Luís"
idade = 32
altura = 1.70

print("Olá me chamo %s e eu tenho %d anos. Minha altura é %f" % (nome, idade, altura))

#Format
print("Olá me chamo {} e eu tenho {} anos. Minha altura é {}".format(nome, idade, altura))
print("Olá me chamo {nome} e eu tenho {idade} anos. Minha altura é {altura}".format(nome=nome, idade=idade, altura=altura))

#F-string
print(f"Olá me chamo {nome} e eu tenho {idade} anos. Minha altura é {altura}")

#Formatando casas decimais
PI = 3.1415
print(f"{PI:.2f}")
print(f"{PI:.4f}")

#Fatiamento de string
nomeProf = "Luís Fernando de Liz Varela"

print(nomeProf[0])
print(nomeProf[:4])
print(nomeProf[4:])
print(nomeProf[:])
print(nomeProf[::-1])
print(nomeProf[-1])

#String múltiplas linhas (triplas)
empresa = "Apple"
instituicao = f"""
Aqui é o 
banco do Brasil
"""

print(empresa)
print(instituicao)