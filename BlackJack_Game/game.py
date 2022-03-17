from engine import  Game, Player

jogador1 = Player('Bruno',1000)
print(jogador1)

lets = True
while lets:
    Game(jogador1)
    
    if input("Mais uma rodada?\n pressione s para jogar ou n para parar: ") == 'n':
        print(f'\n\n Obrigado por jogar, você saiu com {jogador1.dinheiro}$')
        lets = False