#São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória
curso = "Curso de Python"
nome_curso = curso

saldo , limite = 200,200

print(curso is nome_curso)


print(curso is not nome_curso)

#Ocupa a mesma região de memoria?
print(saldo is limite)


