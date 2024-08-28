import pygame

from data.script.botao import Botoes

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
        self.bg_color = (47, 79, 79)

        #grade
        self.rows = 4
        self.cols = 3
        self.espacamento = 20
        self.grade_cor = (119, 136, 153)

        #carta
        self.cor_carta = (245, 245, 220)
        self.cor_texto = (0, 0, 0)

        #botoes
        self.centro_tela = self.janela_rect.centery
        x = self.janela_rect.centerx

        self.facil = Botoes(self, "Facil", x, self.centro_tela - 75)
        self.medio = Botoes(self, "Médio", x, self.centro_tela)
        self.dificil = Botoes(self, "Difícil", x, self.centro_tela + 75)
        self.comojogar = Botoes(self, "Como jogar?", x, self.centro_tela + 150)
        self.botao_pausa = Botoes(self, "Pausar", self.janela_rect.width - 160, 40)
        self.botao_despausa = Botoes(self, "Despausar", self.janela_rect.width - 160, 40)
        self.voltar_menu = Botoes(self, "Menu", x, self.janela_rect.height - 100)
        self.voltar_menu_jogo = Botoes(self, "Menu", self.janela_rect.width - 160, self.janela_rect.height - 60)

        botoes = self.janela_rect.height // 3 * 2
        self.botoes = [
            Botoes(self, "Verdade", x, botoes),
            Botoes(self, "Não tenho certeza", x, botoes + 60),
            Botoes(self, "Mentira", x, botoes + 120)
        ]

        self.set_dificuldade(4, 3)

    def _recalcular_tamanhos(self):
        self.quadrado_largura = (self.janela_largura - 2 * self.margem - self.espacamento * (self.cols + 1)) // self.cols
        self.quadrado_altura = (self.janela_altura - 2 * self.margem - self.espacamento * (self.rows + 1)) // self.rows

    def set_dificuldade(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self._recalcular_tamanhos()
