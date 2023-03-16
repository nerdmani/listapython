ml = [17, 8, 10, 6, 2, 4] #Lista para ordenar
trocado = True #precisamos dele para entrar no Loop While

while trocado:
    trocado = False #sem trocas até agora
    for i in range(len(ml)-1):
        if ml [i] > ml [i+1]: 
            trocado = True #ocorreu uma troca!
            ml[i], ml[i + 1] = ml[i +1], ml[i]
print(ml)