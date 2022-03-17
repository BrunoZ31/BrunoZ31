import random 
import time
from IPython.display import clear_output
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':14}

class Card:

    def __init__(self, rank,suit):
        self.suit = suit
        self.rank = rank
    
    def valor(self,soma=0,isd=False):
        if self.rank == 'Ace': # escolha do valor do ACE
            loop_ace = True
            if isd:
                if soma > 10:
                    self.value = 1
                else:
                    self.value = 11
            else:
                while loop_ace:
                    resposta = input("Ace como 11 ou 1: ")

                    if resposta == '11':
                        self.value = 11
                        loop_ace = False

                    elif resposta == '1':
                        self.value = 1
                        loop_ace = False

                    else:
                        print("resposta não foi 1 ou 11")
            
            return self.value
        
        else: # caso não for um ACE o valor é o do dicionário values
            
            self.value = values[self.rank]
            return self.value

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for nipe in suits: # constroi o deck
            for numero in ranks:
                self.all_cards.append(Card(numero,nipe))
                
    def shuffle(self): # não retorna
        random.shuffle(self.all_cards)
        
    def deal_one(self): # remove uma da lista all cards
        return self.all_cards.pop() 

class Player:
    
    def __init__(self, name, account):
        self.nome = name
        self.dinheiro = account
    
    def money(self,variacao):
        self.dinheiro += variacao # adapta a carteira a perdas e ganhos
    
    def __str__(self):
        return 'O jogador ' + self.nome + ' tem ' + str(self.dinheiro) + '$'

def stayhit(): 
    loop_sh = True

    while loop_sh: 
        play=input("stand(s) ou hit(h): ")

        if play == 'h':
            return(True)
        
        elif play == 's':
            return(False)

def aposta():
    loop_bet = True
    
    while loop_bet: # loop para garantir que aposta seja float
        try:
            bet = float(input("Qual sua aposta: "))
            if bet > 0:
                loop_bet = False
        
        except:
            print('not a number ou menor do que zero')
    
    return(bet)

class Game:
    
    def __init__(self,player):
        game_on_p = True
        clear_output()
        
        baralho = Deck() #posiciona o baralho novo
        baralho.shuffle() # embaralha
        
        print(f"\n\nComeço de rodada, o jogador tem {player.dinheiro}$")
            
        # APOSTA
        loop_aposta = True

        while loop_aposta:
            bet = aposta()
            
            if player.dinheiro - bet < 0:
                print("ta querendo apostar mais do que tem")
            
            else:
                loop_aposta = False
        
        self.aposta = bet 
    
        mesa_p = []
        mesa_d = []

        for i in range(2):
            mesa_p.append(baralho.deal_one())
        mesa_d.append(baralho.deal_one())
        
        # RODADA
        
        while game_on_p:
            
            # Player
            print("\nAs cartas na mesa do player são:\n")
            
            soma_p = 0
            for carta_mesa in mesa_p:
                print(carta_mesa)
                soma_p += carta_mesa.valor()
            print(f"\nDealer possui {mesa_d[0]}, de valor {mesa_d[0].valor()}")
            
            print(f'\nSoma total do player é {soma_p}\n')
            
            if soma_p > 21:
                print('passou de 21, o deler ganhou')  
                player.money(-self.aposta)
                break
            
            game_on_p = stayhit()
            
            carta_sacada = baralho.deal_one()
            mesa_p.append(carta_sacada)
            
        # Dealer
            
        game_on_d = not game_on_p
        while game_on_d:
            carta_sacada = baralho.deal_one()
            mesa_d.append(carta_sacada)

            print("\nAs cartas do dealer na mesa são:\n")

            soma_d = 0
            for carta_mesa in mesa_d:
                print(carta_mesa)
                soma_d += carta_mesa.valor(soma_d,True)
                time.sleep(1)
            
            print(f'\nSoma total do Dealer é {soma_d}')

            if soma_d > 21:
                print(f'\nDealer passsou de 21\n\n\nVocê GANHOU {str(self.aposta)}$\n\n')
                player.money(self.aposta)                
                break
            if soma_d == soma_p:
                print('\nEmpatou\n')
                break
            
            if soma_d > soma_p:
                print('\nO dealer ganhou\n')
                player.money(-self.aposta)
                break
                