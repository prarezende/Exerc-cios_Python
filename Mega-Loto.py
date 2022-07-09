#Gerando numeros aleatórios

from random import randint

print(' Sugestão Mega-Sena')
for i in range(6):
    print (randint(0,60))
print(' Sugestão Loto Fácil')
for i in range(15):
    print (randint(1,25))
print(' Boa Sorte!!!!')
    
        
#for num in range(1,26):
#    print ('Carregando', num)

# com sample os numeros não se repetem

from random import sample

sorteados = sample(range(0, 61), 6)
sorteados.sort()
print('Outra Mega-Sena', sorteados)

lotofacil = sample(range(1,26), 15)
lotofacil.sort()
print('Lotofácil ', lotofacil)

