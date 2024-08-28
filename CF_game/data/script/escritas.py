import pygame

class Escrevendo:
    def __init__(self, cf_game):
        self.cf_game = cf_game
        self.config = self.cf_game.config
        self.janela = self.cf_game.janela
        self.cor_texto = (255, 255, 255)
        self.cor = self.config.bg_color
        pygame.font.init()
        self.font = pygame.font.SysFont("Impact", 72)

        self.msg = None

    def escrever(self, msg, largura_carta):
        self.msg = msg
        if self.msg:
            self.msg_imagem = self.font.render(self.msg, True, self.cor_texto, self.cor)
            self.msg_imagem_rect = self.msg_imagem.get_rect()
            self.msg_imagem_rect.centerx = largura_carta // 2
            self.msg_imagem_rect.y = 100
            self.janela.blit(self.msg_imagem, self.msg_imagem_rect)