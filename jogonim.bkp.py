def main():
    while True:
        jogo = int(input("Escolha um modo de jogo!"))
        if jogo == 1:
            partida()
        if jogo == 2:
            campeonato()
        

            
def usuario_escolhe_jogada(n,m):
    limite = m
    num = int(input("Inisira o numero de peças que deseja retirar do tabuleiro: "))
    while num > limite or num < 0 or num  == 0 :
        print("Valor inválido! ")
        num = int(input("Inisira o numero de peças que deseja retirar do tabuleiro: "))
    if num > n:
        num = n 
    return num

def computador_escolhe_jogada(n,m):
    limite = m
    if n < m:
        m = n
    else:
        m
    return m

def partida():
    n = int(input("Insira o numero de peças do tabuleiro: "))
    m = int(input("Insira o número máximo de peças a serem retiradas por jogada"))
    if  m < 0 or n < 0 :
        print("Valores insvalidos!!")
        partida()
    if n % (m+1) == 0 or n < m:
        print ("Usuário escolhe jogada!")
        while n >= 0:
            p = usuario_escolhe_jogada(n,m)
            n = n - p
            print("O usuário retirou",p,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("O usuario veceu!")
                break
            p = computador_escolhe_jogada(n,m)
            n = n - p
            print("O computadore retirou",p,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("O computador veceu!")
                break
    else:
        print ("computador secolhe jogada")
        while n >= 0:
            p = computador_escolhe_jogada(n,m)
            n = n - p
            print("O computadore retirou",p,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("O computador veceu!")
                break
            p = usuario_escolhe_jogada(n,m)
            n = n - p
            print("O usuário retirou",p,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("O usuario veceu!")
                break
            
        
def campeonato():
    print("Modo campeonato")
    champs = 4
    while champs > 0:
        champs = champs - 1
        if champs == 0:
            break
        partida()
        
    
main()

