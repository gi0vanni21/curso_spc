jogos = [
    'pokemon',
    'super mario',
    'sonic',
    'cod',
    'cs go',

]

#imprimindo apenas o sonic
print(jogos[2])

#imprimindo apenas o super mario
print(jogos[1])


#imprimindo apenas o pokemon
print(jogos[0])


print(f'o tamannho da lista jogos é {len(jogos)} ')


#utilizando lista
for jogo in jogos:
    print(f'o jogo {jogo} é muito arretado!')


#utilizando o conceito de vetor
for i in range(len(jogos)):
    print(f'[{i+1}]{jogos[i]}')