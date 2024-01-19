lista = [1,2,3,4,5,6,7,8,9]
pares= []
for i in range(len(lista)):
    if lista[i]%2 == 0:
        pares.append(lista[i])
    print(pares)