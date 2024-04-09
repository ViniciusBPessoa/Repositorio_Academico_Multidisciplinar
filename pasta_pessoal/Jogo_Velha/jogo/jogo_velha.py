class jogo_velha:
    def __init__(self, players = ['X', 'O']) -> None:
        """
        Inicializa o objeto jogo_velha.

        Parameters:
        players (list, optional): Uma lista de dois elementos representando os jogadores do jogo. 
            O padrão é ['X', 'O'].
        """
        self.tabuleiro = ['N' for i in range(9)]
        self.players = players


    # verify if one of the players wins the game
    def victory_checker(self):

        """
        Verifica se algum dos jogadores ganhou o jogo.

        Retorna:
        str: O jogador vencedor ('X', 'O') ou 'N' se não houver vencedor.
        """

        # Listas de combinações de vitória
        victory_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]              # Diagonais
        ]
        winer = 'N'
        
        for combination in victory_combinations:                        # passa por todas as combnaçoes de possiveis vitorias
            for player in self.players:                                 # Passa por todos os players para verificar sua vitoria
                verifyer = True                                         
                for analitc_position in combination:                    # Para cada possivel combnação verifica se a mesma esta completa
                    if self.tabuleiro[analitc_position] != player:
                        verifyer = False                                # caso errado
                        break

                if verifyer:
                    winer = player                                      # caso perfeito
                    break
    
        return winer
    
    def stap(self, location, player):    
        """
        Realiza uma jogada no jogo.

        Parameters:
        location (int): A posição no tabuleiro onde a jogada será feita (de 1 a 9).
        player (int): O índice do jogador que está fazendo a jogada na lista de jogadores.

        Returns:
        None
        """
        location -= 1
        player -= 1

        if self.tabuleiro[location] == "N":
            self.tabuleiro[location] = self.players[player]
    
    def reset(self, players = ['X', 'O']):
        self.tabuleiro = ['N' for i in range(9)]
        self.players = players

test_tab = jogo_velha()
test_tab.tabuleiro = ['X', 'X', 'N', 'N', 'X', 'N', 'N', 'N', 'N']

print(test_tab.tabuleiro)
print(test_tab.victory_checker())
print("-"*50)

test_tab.stap(8, 1)
print(test_tab.tabuleiro)
print(test_tab.victory_checker())
print("-"*50)

test_tab.reset()
print(test_tab.tabuleiro)
