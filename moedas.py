import faker
import random

class pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.lado = None
        self.vitorias = 0
        

def gerar_nome():
    fake = faker.Faker()
    nome = fake.name()
    print(nome)
    return nome

def retorna_zero_ou_um():
    return random.randint(0, 1)


play = []
num_play = 1000
rodadas = 0

for x in range(num_play):
    play.append(pessoa(gerar_nome()))
    
print([x.nome for x in play])
    
def jogo_moeda(jogadores):
    random.shuffle(jogadores)
    jogadores[0].lado = 0
    jogadores[1].lado = 1
    
    resultado = retorna_zero_ou_um()
    
    jogadores[resultado].vitorias += 1
    return jogadores[resultado]

while len(play) != 1:
    
    play2 = []
    random.shuffle(play)
    
    if len(play) % 2 == 0:
        for x in range(0, len(play), 2):
            play2.append(jogo_moeda([play[x], play[x+1]]))
    else:
        play2.append(play[-1])
        play.pop(-1)
        for x in range(0, len(play), 2):
            play2.append(jogo_moeda([play[x], play[x+1]]))
    
    rodadas += 1
    play = play2[:]
    

print(play[0].nome, play[0].vitorias)
print("Rodadas: ", rodadas)