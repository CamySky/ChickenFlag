import pygame.font

class Botoes:

    def __init__(self, cf_game, msg, x_pos, y_pos):
        self.janela = cf_game.janela
        self.janela_rect = self.janela.get_rect()

        self.largura, self.altura = 300, 50
        self.cor_botao = (46, 139, 89)
        self.cor_texto = (255, 255, 255)
        self.font = pygame.font.SysFont("Impact", 36)

        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = x_pos
        self.rect.centery = y_pos
        self.msg = msg

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_imagem = self.font.render(msg, True, self.cor_texto, self.cor_botao)
        self.msg_imagem_rect = self.msg_imagem.get_rect()
        self.msg_imagem_rect.center = self.rect.center

    def draw_botao(self):
        self.janela.fill(self.cor_botao, self.rect)
        self.janela.blit(self.msg_imagem, self.msg_imagem_rect)


