'''
    Iterando strings com while
'''

#   012345678910
'''
nome = 'Luiz Otávio' # Iteráveis

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])
'''

nome = 'Luiz Gustavo'
I = 0
novo_nome = ''


while I < len(nome):
    letra = nome[I]
    novo_nome += f'*{letra}'
    print(nome[I])
    I += 1
novo_nome += '*'    
print(novo_nome)    