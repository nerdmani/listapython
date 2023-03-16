#etapa 1
banda = []
print('Etapa 1', banda)

#etapa 2:
banda.append("John Lennon")
banda.append('Paul McCarteney')
banda.append('George Harrison')
print('Etapa 2: ', banda)

#etapa 3:
for members in range(2):
    banda.append(input('Novo membro: '))
print('Etapa 3: ', banda)

#etapa 4:
del banda[-1]
del banda[-1]
print('Etapa 4: ', banda)

#etapa 5: 
banda.insert(0, 'RigonStarr')
print("Etapa 5:", banda)
print('The Fab:', len(banda))