import pygame

class Config:
    
    def __init__(self, cf_game):
        pygame.init()
        tela_info = pygame.display.Info()
        self.cf_game = cf_game

        #tela
        self.janela = self.cf_game.janela
        self.janela_rect = self.janela.get_rect()
        self.margem = 90
        self.janela_largura = tela_info.current_w
        self.janela_altura = tela_info.current_h
        self.bg_color = (216, 163, 243) #lilás

        #escritas
        self.cor_text = (50, 50, 50)

        #botoes
        self.btn_altura = 50
        self.btn_largura = 300
        self.btn_cor = (243, 187, 163)
        self.btn_cor_text = (50, 50, 50)

        #grade
        self.rows = 4
        self.cols = 3
        self.espacamento = 20
        self.grade_cor = (163, 243, 179)#verde pastel

        #carta
        self.cor_carta = (245, 245, 220)
        self.cor_texto = (0, 0, 0)

        self.set_dificuldade(4, 3)

    def _recalcular_tamanhos(self):
        self.quadrado_largura = (self.janela_largura - 2 * self.margem - self.espacamento * (self.cols + 1)) // self.cols
        self.quadrado_altura = (self.janela_altura - 2 * self.margem - self.espacamento * (self.rows + 1)) // self.rows

    def set_dificuldade(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self._recalcular_tamanhos()
