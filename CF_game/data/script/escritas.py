import pygame

class Escrevendo:
    def __init__(self, cf_game):
        self.config = cf_game.config
        self.janela = cf_game.janela
        self.cor_texto = self.config.cor_text
        self.cor_bg = self.config.bg_color
        self.msg_imagem_rect = None

    def escrever_carta(self, msg, largura_carta):
        font = pygame.font.SysFont("Impact", 42)
        if msg:
            self.msg_imagem = font.render(msg, True, self.cor_texto, self.cor_bg)
            self.msg_imagem_rect = self.msg_imagem.get_rect()
            self.msg_imagem_rect.centerx = largura_carta // 2
            self.msg_imagem_rect.y = 100
            self.janela.blit(self.msg_imagem, self.msg_imagem_rect)

    def escrever_centro_acima(self, msg, tam_letra):
        font = pygame.font.SysFont("Impact", tam_letra)
        self.msg_imagem = font.render(msg, True, self.cor_texto, self.cor_bg)
        self.msg_imagem_rect = self.msg_imagem.get_rect()
        self.msg_imagem_rect.centerx = self.config.janela_largura // 2
        self.msg_imagem_rect.centery = 80
        self.janela.blit(self.msg_imagem, self.msg_imagem_rect)

    def escrever_canto_dir_acima(self, msg):
        font = pygame.font.SysFont("Impact", 42)
        self.msg_imagem = font.render(msg, True, self.cor_texto, self.cor_bg)
        self.msg_imagem_rect = self.msg_imagem.get_rect()
        self.msg_imagem_rect.centerx = self.config.janela_largura // 4
        self.msg_imagem_rect.centery = 80
        self.janela.blit(self.msg_imagem, self.msg_imagem_rect)

    def escerver_segundo_plano(self, msg):
        font = pygame.font.SysFont("Impact", 42)
        largura_fundo = 600
        altura_fundo = 200
        x_fundo = (self.config.janela_largura - largura_fundo) // 2
        y_fundo = (self.config.janela_altura - altura_fundo) // 2
        pygame.draw.rect(self.janela, (163, 243, 223), (x_fundo, y_fundo, largura_fundo, altura_fundo))
        confirm_imagem = font.render(msg, True, self.cor_bg)
        confirm_rect = confirm_imagem.get_rect(center=self.janela.get_rect().center)
        confirm_rect.center = (x_fundo + largura_fundo // 2, y_fundo + altura_fundo // 2)
        self.janela.blit(confirm_imagem, confirm_rect)
