class jogo_velha:
    def __init__(self, players = ['X', 'O']) -> None:
        self.tabuleiro = ['N' for i in range(9)]
        self.players = players


    # verify if one of the players wins the game
    def victory_checker(self):
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

                if verifyer:
                    winer = player
    
        return winer
    
    def stap(self, location, player):              
        if self.tabuleiro[location-1] == "N":
            self.tabuleiro[location-1] = self.players[player]

test_tab = jogo_velha()
print(test_tab.tabuleiro)