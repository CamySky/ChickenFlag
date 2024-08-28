import pygame
import random

class Grade:

    def __init__(self, cf_game):
        self.cf_game = cf_game
        self.janela = cf_game.janela
        self.config = cf_game.config
        self.dicas = cf_game.dicas
        self.img_interrogacao = pygame.image.load('data/img/Interrogacao.bmp')
        self.update_dimensions()
        self.used_tips = set()
        self.cores_quadrados = [[self.config.grade_cor for _ in range(self.cols)] for _ in range(self.rows)]

    def update_dimensions(self):
        self.cor = self.config.grade_cor
        self.quadrado_altura = self.config.quadrado_altura
        self.quadrado_largura = self.config.quadrado_largura
        self.espacamento = self.config.espacamento
        self.rows = self.config.rows
        self.cols = self.config.cols
        self.margem = self.config.margem
        self.paises_aleatorios = self.dicas.paises_aleatorios
        self.interrogacao = pygame.transform.scale(self.img_interrogacao , (self.quadrado_largura, self.quadrado_altura))
        if self.cf_game.prin_mov == True:
            self.cores_quadrados = [[self.config.grade_cor for _ in range(self.cols)] for _ in range(self.rows)]

    def draw_grid(self):
        self.update_dimensions()
        for row in range(self.rows):
            for col in range(self.cols):
                x = self.margem + self.espacamento + col * (self.quadrado_largura + self.espacamento)
                y = self.margem + self.espacamento + row * (self.quadrado_altura + self.espacamento)
                if row == 0:
                    self.janela.blit(self.interrogacao, (x, y))
                else:
                    pygame.draw.rect(self.janela, self.cores_quadrados[row][col], (x, y, self.quadrado_largura, self.quadrado_altura))

    def get_tip_by_col(self, col):
        if col < len(self.paises_aleatorios):
            tips = self.paises_aleatorios[col]["tips"]
            available_tips = [tip for tip in tips if tip not in self.used_tips]

            if not available_tips:
                available_tips = tips
                self.used_tips = set()

            chosen_tip = random.choice(available_tips)
            self.used_tips.add(chosen_tip)
            return chosen_tip
        else:
            return None

    def update(self):
        self.update_dimensions()
        self.draw_grid()
