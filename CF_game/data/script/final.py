import pygame
import time

class Finalizando:
    def __init__(self, cf_game):
        self.cf_game = cf_game
        self.janela = cf_game.janela
        self.dicas = cf_game.dicas
        self.chicken = cf_game.chicken
        self.escrevendo = cf_game.escrevendo
        self.tempo_inicial = time.time()
        self.venceu = True
        self.pontos = 0

    def pontos_finais(self):
        if self.dicas.paises_aleatorios[self.chicken.cols]["nome"] == self.dicas.pais_nome:
            self.pontos += 200
            self.text = "Vitória!!!"
        else:
            self.pontos -= 200
            self.text = "Derrota..."

        tempo_decorrido = self.cf_game.tempo_decorrido
        if tempo_decorrido < 60:
            self.pontos += 50
        elif tempo_decorrido < 120:
            self.pontos += 30
        else:
            self.pontos += 10

    def pontos_por_dificuldade(self, dificuldade):
        if dificuldade == "facil":
            self.pontos += 50
        elif dificuldade == "medio":
            self.pontos += 100
        else:
            self.pontos += 150

    def adicionar_pontos_resposta(self, correta, tipo_resposta):
        if correta:
            if tipo_resposta == "Verdade":
                self.pontos += 50
                print("Pontos para resposta correta")
            elif tipo_resposta == "Mentira":
                self.pontos -= 30
                print("Penalidade para negar incorretamente")
        else:
            if tipo_resposta == "Verdade":
                self.pontos -= 30
                print("Penalidade para resposta errada")
            elif tipo_resposta == "Mentira":
                self.pontos += 50
                print("Pontos para negar corretamente")

    def resultado(self):
        arqImg = self.dicas.paises_aleatorios[self.chicken.cols]["bandeira"]
        bandeira = pygame.image.load(arqImg)

        largura_janela, altura_janela = self.janela.get_size()
        largura_imagem, altura_imagem = bandeira.get_size()

        x_pos = (largura_janela - largura_imagem) // 2
        y_pos = (altura_janela - altura_imagem) // 2

        self.janela.blit(bandeira, (x_pos, y_pos))
        self.escrevendo.escrever_centro_acima(self.text, 42)
