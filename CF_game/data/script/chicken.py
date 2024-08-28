import pygame

class Chicken:
    def __init__(self, cf_game):
        self.cf_game = cf_game
        self.janela = cf_game.janela
        self.config = cf_game.config
        self.janela_rect = cf_game.janela.get_rect()

        self.image = pygame.image.load('data/img/chicken-sem-fundo.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = (self.janela_rect.centerx, self.janela_rect.bottom)

        self.rows = (self.config.rows)
        self.cols = self.config.cols

    def mover(self, px, py):
        if(self.cf_game.prin_mov == True):
            self.atualizar_configuracoes()
        self.rows += px
        self.cols += py
        self.rows = max(0, min(self.rows, self.config.rows - 1))
        self.cols = max(0, min(self.cols, self.config.cols - 1))
        self._nova_posicao()

    def _nova_posicao(self):
        # Calcula a nova posição centralizada no quadrado atual
        x = self.config.margem + self.config.espacamento + self.cols * (self.config.quadrado_largura + self.config.espacamento) + self.config.quadrado_largura // 2
        y = self.config.margem + self.config.espacamento + self.rows * (self.config.quadrado_altura + self.config.espacamento) + self.config.quadrado_altura // 2
        self.rect.center = (x, y)

    def atualizar_configuracoes(self):
        self.rows = self.config.rows
        self.cols = self.config.cols

    def blitme(self):
        self.janela.blit(self.image, self.rect)
