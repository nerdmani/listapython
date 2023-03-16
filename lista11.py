#Criando lista com lista com elementos duplicados 
lcd = [1,2,3,1,4,2,5,6,3,7,8,5,9]

#Inicializando uma lista vazia para armazenar os elemntos único
lsd = []

#Usando um loop while para percorrer a lista e remover os elementos duplicados
while lcd:
    e = lcd.pop(0) #pop é usada para remover o elemento
    if e not in lsd:
        lsd.append(e)

#Imprimindo o resultado
print("A lista sem duplicadas é:", lsd)