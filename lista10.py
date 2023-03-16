#Criando uma lsta de numeros
n = [10,20,30,40,50]

#Inicializando a variavel que ira armazenar o maior numero
mn = n[0]

#Usando o loop for para percorrer a lista e encontrar o maior numero
for n1 in n:
    if n1 > mn:
        mn = n1

#Imprimindo o resultado
print('O maior numero de lista é: ', mn)