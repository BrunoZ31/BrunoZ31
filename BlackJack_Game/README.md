# Blackjack

The game of [Blackjack](https://en.wikipedia.org/wiki/Blackjack) or twenty-one is a casino game where players and the dealer (table) compete for how close they get to 21 without going over it. 

My code allows simulating a player against an automated dealer. The player plays with hit (h) or stand(s), show one more card or stop respectively, and also has a wallet that is established at the beginning, when the player loses all his money he must restart the game or stop to train a little.

One of the recurring features in the game occurs when the card is an ACE, if that is the case, you must choose the one that best fits your deck every time the game runs. The dealer has this automated pick based on your current score. 

Run the game on terminal with:
```bash
python3 game.py
```
In this file you can change the name of the player and the wallet amount
```python
jogador1 = Player('{name}',{wallet amount})
print(jogador1)
```

### Jogo 21

O jogo de  [Blackjack](https://en.wikipedia.org/wiki/Blackjack) ou vinte e um é um jogo de cassino em que os jogadores e o dealear (mesa) disputam o quão próximo chegam de 21 sem ultrapassar.

Meu código permite simular o jogo de só um jogador contra um dealer automatizado. O jogador joga com hit (h) ou stand(s), mostrar mais uma carta ou parar respectivamente, e também possui uma carteira que é estabelecida no começo, quando o jogador perde todo seu dinheiro deve recomeçar o jogo ou parar para treinar um pouco antes de retornar.

Uma das funcionalidades recorrentes no jogo ocorre quando a carta é um ACE, se esse for o caso, deve-se escolher a que melhor se adapta ao seu baralho toda vez que o jogo roda. O dealer tem essa escolha automatizada com base na sua pontuação atual.

Para declarar um jogador
```python
jogador1 = Player('Bruno',1000)
print(jogador1)
```
