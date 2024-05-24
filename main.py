#lista de 15 nomes
nomes = ['Michael','Micaely','Fabio','Tiago','Tatiane','Raylton','Renan','Ana Claudia','Valéria','Bruno','Guilherme','João','Pedro','Bruna','Gabriela']
# usuario informa o nome que deseja pesquisar

nome = input('Digite o nome a ser pesquisado: ').capitalize()


# verifica se o nome está na lista ou não
try:
    # retorna o indice do nome pesquisado
    indice = nomes.index(nome)
    print(f'Nome encontrado: {nome} no índice {indice}.')
except:
    print(f'{nome} não encontrado na lista.')