from random import randint

class Tabuleiro():

    def __init__(self, tamanho_tabuleiro = 8, posicao_inicial = None, profundidade_prospectiva = 3):
        self.tamanho_tabuleiro = tamanho_tabuleiro * tamanho_tabuleiro
        self.tabuleiro = [0 for _ in range(self.tamanho_tabuleiro)] # 0 = casa vazia, 1 = casa ocupada, 2 = casa passada
        self.jogadas_realizadas = []
        self.profundidade_prospectiva = profundidade_prospectiva

        self.posicao_inicial = self.inicializa_tabuleiro(posicao_inicial)

    def jogar_partida_completa(self) -> int:
        """
        Executa o jogo automaticamente até não haver mais jogadas possíveis
        Retorna a pontuação final (número de casas visitadas)
        """
        while self.realizar_jogada():
            continue
        
        return self.verifica_pontuacao()

    def verificar_jogadas(self, tabuleiro: list = None) -> list:
        """
        Retorna todas as jogadas válidas para um cavalo na posição atual
        """
        # Usa o tabuleiro da classe se nenhum for fornecido
        tabuleiro_alvo = tabuleiro if tabuleiro is not None else self.tabuleiro
        
        # Encontra a posição atual do cavalo (onde o valor é 1)
        posicao_cavalo = None
        for i, valor in enumerate(tabuleiro_alvo):
            if valor == 1:  # Casa ocupada pelo cavalo
                posicao_cavalo = i
                break
        
        if posicao_cavalo is None:
            return []  # Cavalo não encontrado no tabuleiro
        
        movimentos = [
            (-2, -1), (-2, 1),  # 2 para cima, 1 esquerda/direita
            (-1, -2), (-1, 2),  # 1 para cima, 2 esquerda/direita
            (1, -2), (1, 2),    # 1 para baixo, 2 esquerda/direita
            (2, -1), (2, 1)     # 2 para baixo, 1 esquerda/direita
        ]
        
        jogadas_validas = []
        
        linha_atual = posicao_cavalo // 8
        coluna_atual = posicao_cavalo % 8
        
        for movimento in movimentos:
            nova_linha = linha_atual + movimento[0]
            nova_coluna = coluna_atual + movimento[1]
            
            if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                nova_posicao = nova_linha * 8 + nova_coluna

                if tabuleiro_alvo[nova_posicao] == 0:
                    jogadas_validas.append(nova_posicao)
        
        return jogadas_validas

    def prospectar_jogadas(self, n_jogadas: int) -> list:
        possiveis_jogadas = self.verificar_jogadas()
        resultados = []

        for jogada in possiveis_jogadas:
            tabuleiro_prospectado = self.tabuleiro.copy()
            pontuacao = self.jogadas_realizadas.copy()
            
            tabuleiro_prospectado[jogada] = 1
            posicao_anterior = self.jogadas_realizadas[-1]
            tabuleiro_prospectado[posicao_anterior] = 2
            pontuacao.append(jogada)

            for _ in range(n_jogadas):
                possiveis_jogadas_simulacao = self.verificar_jogadas(tabuleiro_prospectado)
                if len(possiveis_jogadas_simulacao) == 0:
                    break
                
                jogada_escolhida = possiveis_jogadas_simulacao[randint(0, len(possiveis_jogadas_simulacao) - 1)]
                
                for i, valor in enumerate(tabuleiro_prospectado):
                    if valor == 1:
                        tabuleiro_prospectado[i] = 2
                        break
                
                tabuleiro_prospectado[jogada_escolhida] = 1
                pontuacao.append(jogada_escolhida)
            
            resultados.append(pontuacao)

        if not resultados:
            return []

        max_tamanho = max(len(resultado) for resultado in resultados)
        melhores_jogadas = []

        for i, resultado in enumerate(resultados):
            if len(resultado) == max_tamanho:
                melhores_jogadas.append(possiveis_jogadas[i])

        return melhores_jogadas

    def realizar_jogada(self):
        if len(self.jogadas_realizadas) == 0:
            return False
        
        possiveis_jogadas = self.verificar_jogadas()
        
        if len(possiveis_jogadas) == 0:
            return False
        
        melhores_jogadas = self.prospectar_jogadas(self.profundidade_prospectiva)
        
        if melhores_jogadas:
            jogada_escolhida = melhores_jogadas[randint(0, len(melhores_jogadas) - 1)]
        else:
            jogada_escolhida = possiveis_jogadas[randint(0, len(possiveis_jogadas) - 1)]
        
        posicao_atual = self.jogadas_realizadas[-1]
        
        self.tabuleiro[posicao_atual] = 2
        self.tabuleiro[jogada_escolhida] = 1
        self.jogadas_realizadas.append(jogada_escolhida)
        
        return True

    def verifica_pontuacao(self, pontuacao_gerada = None) -> int:
        if pontuacao_gerada is not None:
            return len(pontuacao_gerada)
        else:
            return len(self.jogadas_realizadas)
        
    def exibir_tabuleiro(self):
        tamanho_linha = self.tamanho_tabuleiro ** 0.5
        for i in range(self.tamanho_tabuleiro):
            if i % tamanho_linha == 0:
                print()
            print(self.tabuleiro[i], end=" ")
        print()

    def inicializa_tabuleiro(self, posicao_inicial):
        """
        Adciona um cavalo a uma posição aeleatoria do tabuleiro
        """
        if posicao_inicial is not None:
            casa_jogada = posicao_inicial
        else:
            casa_jogada = randint(0, self.tamanho_tabuleiro - 1)
        self.tabuleiro[casa_jogada] = 1
        self.jogadas_realizadas.append(casa_jogada)

        return casa_jogada


test = Tabuleiro(profundidade_prospectiva= 30, posicao_inicial=0)
test.exibir_tabuleiro()
print(test.jogadas_realizadas)
print(test.verificar_jogadas())

test.jogar_partida_completa()
test.exibir_tabuleiro()