class jogo_velha:
    def __init__(self, players = ['X', 'O']) -> None:
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
        
        for combination in victory_combinations:
            for player in self.players:
                verifyer = True
                for analitc_position in combination:
                    if self.tabuleiro[analitc_position] != player:
                        verifyer = False
                        break

                if verifyer:
                    winer = player
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
