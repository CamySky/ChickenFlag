import pygame.font


class Botoes:

    def __init__(self, cf_game):
        self.janela = cf_game.janela
        self.janela_rect = self.janela.get_rect()
        config = cf_game.config

        self.font = pygame.font.SysFont("Impact", 36)
        self.cor_texto = config.btn_cor_text
        self.largura = config.btn_largura
        self.altura = config.btn_altura
        self.cor_botao = config.btn_cor
        self.msg = None
        self.msg_imagem = None
        self.msg_imagem_rect = None
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)

    def btn_facil(self):
        self.msg = "Fácil"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        x = self.janela_rect.centerx
        y = self.janela_rect.centery
        self.rect.centerx = x
        self.rect.centery = y - 75
        self.cor_botao = (173, 216, 230) #Azul pastel
        self.msg_get()
        self.btn_draw()
        return self.rect

    def btn_medio(self):
        self.msg = "Médio"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = self.janela_rect.centerx
        self.rect.centery = self.janela_rect.centery
        self.cor_botao = (253, 253, 150)#Amarelo pastel
        self.msg_get()
        self.btn_draw()
        return self.rect

    def btn_dificil(self):
        self.msg = "Difícil"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = self.janela_rect.centerx
        self.rect.centery = self.janela_rect.centery + 75
        self.cor_botao = (255, 182, 193) #Rosa pastel
        self.msg_get()
        self.btn_draw()
        return self.rect

    def btn_comoJogar(self):
        self.msg = "Como jogar?"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = self.janela_rect.centerx
        self.rect.centery = self.janela_rect.centery + 150
        
        self.msg_get()
        self.btn_draw()
        return self.rect

    def btn_pausar(self):
        self.msg = "Pausar"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = self.janela_rect.width - 160
        self.rect.centery = 40
        
        self.msg_get()
        self.btn_draw()
        return self.rect

    def btn_despausar(self):
        self.msg = "Despausar"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = self.janela_rect.width - 160
        self.rect.centery = 40
        
        self.msg_get()
        self.btn_draw()
        return self.rect

    def btn_menu(self):
        self.msg = "Menu"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = self.janela_rect.centerx
        self.rect.centery = self.janela_rect.height - 100
        
        self.msg_get()
        self.btn_draw()
        return self.rect

    def btn_menuBack(self):
        self.msg = "Menu"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = self.janela_rect.width - 160
        self.rect.centery = self.janela_rect.height - 60
        
        self.msg_get()
        self.btn_draw()
        return self.rect

    def btn_vdd(self):
        self.msg = "Verdade"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = self.janela_rect.centerx
        self.rect.centery = self.janela_rect.height // 3 * 2
        
        self.msg_get()
        self.btn_draw()
        return self.rect

    def btn_talvez(self):
        self.msg = "Talvez"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = self.janela_rect.centerx
        self.rect.centery = self.janela_rect.height // 3 * 2 + 60
        
        self.msg_get()
        self.btn_draw()
        return self.rect

    def btn_mentira(self):
        self.msg = "Mentira"
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.centerx = self.janela_rect.centerx
        self.rect.centery = self.janela_rect.height // 3 * 2 + 120
        
        self.msg_get()
        self.btn_draw()
        return self.rect

    def msg_get(self):
        self.msg_imagem = self.font.render(self.msg, True, self.cor_texto, self.cor_botao)
        self.msg_imagem_rect = self.msg_imagem.get_rect()
        self.msg_imagem_rect.center = self.rect.center

    def btn_draw(self):
        pygame.draw.rect(self.janela, self.cor_botao, self.rect, border_radius=20)
        self.janela.blit(self.msg_imagem, self.msg_imagem_rect)