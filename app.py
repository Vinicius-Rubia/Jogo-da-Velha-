tabela = ['_','_','_','_','_','_','_','_','_']

def desenha_tabela(campo_velha):
    jogo_velha = ''
    for i in range(len(campo_velha)):
        if(i == 2 or i == 5 or i == 8):
            jogo_velha += " " + campo_velha[i] + " \n"
        else:
            jogo_velha += " " + campo_velha[i] + " |"
    return jogo_velha

def verifica_tabela(campo_velha, posicao):
    resultado = False
    if(campo_velha[posicao] == '_'):
        resultado = True
    return resultado

def verifica_vitoria(campo_velha, simbolo):
    resultado = False
    # Linha
    if(campo_velha[0] == simbolo and campo_velha[1] == simbolo and campo_velha[2] == simbolo):
        resultado = True
    elif(campo_velha[3] == simbolo and campo_velha[4] == simbolo and campo_velha[5] == simbolo):
        resultado = True
    elif(campo_velha[6] == simbolo and campo_velha[7] == simbolo and campo_velha[8] == simbolo):
        resultado = True
    # Coluna
    elif(campo_velha[0] == simbolo and campo_velha[3] == simbolo and campo_velha[6] == simbolo):
        resultado = True
    elif(campo_velha[1] == simbolo and campo_velha[4] == simbolo and campo_velha[7] == simbolo):
        resultado = True
    elif(campo_velha[2] == simbolo and campo_velha[5] == simbolo and campo_velha[8] == simbolo):
        resultado = True
    # Diagonal
    elif(campo_velha[0] == simbolo and campo_velha[4] == simbolo and campo_velha[8] == simbolo):
        resultado = True
    elif(campo_velha[6] == simbolo and campo_velha[4] == simbolo and campo_velha[2] == simbolo):
        resultado = True
    return resultado

# verificar o empate
def verificar_empate(campo_velha):
    resultado = True
    for i in campo_velha:
        if(i == '_'):
            resultado = False
    return resultado

# Variaveis do jogo
jogador = 1
jogador_numero_1 = 0
jogador_numero_2 = 0

while(True):
    # verifica se é a vez do jogador 1
    if(jogador == 1):
        jogador_numero_1 = input('Jogador 1 Digite uma posição de 1 a 9 : ')
        if(verifica_tabela(tabela, int(jogador_numero_1)-1)):
            tabela[int(jogador_numero_1)-1] = 'X'
            jogador = 2
            print(desenha_tabela(tabela))
        else :
            print(desenha_tabela(tabela))
            print('Posicao ja ocupada')
    if(verifica_vitoria(tabela,'X')):
        print('Jogador numero 1 ganhou')
        break
    if(verificar_empate(tabela)):
        print('Empate')
        break
    
    # verifica se é a vez do jogador 2
    if(jogador == 2):
        jogador_numero_2 = input('Jogador 2 Digite uma posição de 1 a 9 : ')
        if(verifica_tabela(tabela,int(jogador_numero_2)-1)):
            tabela[int(jogador_numero_2)-1] = 'O'
            jogador = 1
            print(desenha_tabela(tabela))
        else :
            print(desenha_tabela(tabela))
            print('Posicao ja ocupada')
    if(verifica_vitoria(tabela,'O')):
        print('Jogador numero 2 ganhou')
        break
    if(verificar_empate(tabela)):
        print('Empate')
        break