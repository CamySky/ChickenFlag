import pygame
import time
class Finalizando:
    def __init__(self, cf_game):
        self.cf_game = cf_game
        self.janela = cf_game.janela
        self.pontos = 0
        self.dicas = cf_game.dicas
        self.chicken = cf_game.chicken
        self.tempo_inicial = time.time()
        self.venceu = True

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

    def draw_pontos(self, janela, font):
        pontos_text = f"Pontos: {self.pontos}"
        pontos_imagem = font.render(pontos_text, True, (255, 255, 255))
        janela.blit(pontos_imagem, (10, 60))

    def resultado(self):
        arqImg = self.dicas.paises_aleatorios[self.chicken.cols]["bandeira"]
        bandeira = pygame.image.load(arqImg)

        largura_janela, altura_janela = self.janela.get_size()
        largura_imagem, altura_imagem = bandeira.get_size()

        x_pos = (largura_janela - largura_imagem) // 2
        y_pos = (altura_janela - altura_imagem) // 2

        self.janela.blit(bandeira, (x_pos, y_pos))

        font =pygame.font.SysFont(None, 38)

        resultado_imagem = font.render(self.text, True, (255, 255, 255))
        self.janela.blit(resultado_imagem, (x_pos, y_pos - 50))
