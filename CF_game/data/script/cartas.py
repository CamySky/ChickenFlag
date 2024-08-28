import pygame

from data.script.botao import Botoes


class Cartas:
    def __init__(self, cf_game):
        self.cf_game = cf_game
        self.janela = cf_game.janela
        self.config = cf_game.config
        self.chicken = cf_game.chicken
        self.dicas = cf_game.dicas
        self.grade = cf_game.grade
        self.finalizando = cf_game.finalizando
        self.janela_altura = self.config.janela_altura
        self.janela_largura = self.config.janela_largura
        self.cor = self.config.cor_carta
        self.cor_texto = self.config.cor_texto
        self.font = pygame.font.SysFont(None, 48)
        self.msg = None
        self.msg_imagem = None
        self.mostrando_carta = False
        self.botoes = []

    def _draw_carta(self, col):
        if not self.mostrando_carta:
            self.msg = self.grade.get_tip_by_col(col)
        self.coluna_atual = col
        largura_carta = 500
        altura_carta = 600
        x = (self.janela_largura - largura_carta) // 2
        y = (self.janela_altura - altura_carta) // 2
        pygame.draw.rect(self.janela, self.cor, (x, y, largura_carta, altura_carta))
        self.mostrando_carta = True
        self._info_carta(col, x, y, largura_carta, altura_carta)

    def _quebrar_texto(self, texto, largura_max):
        palavras = texto.split(' ')
        linhas = []
        linha_atual = []
        largura_atual = 0

        for palavra in palavras:
            largura_palavra, _ = self.font.size(palavra + ' ')
            if largura_atual + largura_palavra <= largura_max:
                linha_atual.append(palavra)
                largura_atual += largura_palavra
            else:
                linhas.append(' '.join(linha_atual))
                linha_atual = [palavra]
                largura_atual = largura_palavra
        if linha_atual:
            linhas.append(' '.join(linha_atual))

        return linhas

    def _info_carta(self, col, x, y, largura_carta, altura_carta):
        if self.msg:
            linhas = self._quebrar_texto(self.msg, largura_carta - 20)
            y_offset = y + 20  # Distância do topo da carta

            for linha in linhas:
                linha_imagem = self.font.render(linha, True, self.cor_texto, self.cor)
                linha_imagem_rect = linha_imagem.get_rect()
                linha_imagem_rect.x = x + 10  # Distância das bordas laterais
                linha_imagem_rect.y = y_offset
                self.janela.blit(linha_imagem, linha_imagem_rect)
                y_offset += linha_imagem_rect.height + 5  # Espaçamento entre linhas

            for botao in self.config.botoes:
                botao.draw_botao()

    def draw(self):
        if self.mostrando_carta:
            self._draw_carta(self.chicken.cols)

    def check_click_botao(self, mouse_pos, rows):
        for botao in self.config.botoes:
            if botao.rect.collidepoint(mouse_pos):
                if self.dicas.pais_nome == self.dicas.paises_aleatorios[self.chicken.cols]["nome"]:
                    correta = True
                else:
                    correta = False
                self.finalizando.adicionar_pontos_resposta(correta, botao.msg)
                if botao.msg == "Verdade":
                    self.grade.cores_quadrados[rows][self.coluna_atual] = (0, 209, 28)
                elif botao.msg == "Não tenho certeza":
                    self.grade.cores_quadrados[rows][self.coluna_atual] = (209, 174, 0)
                elif botao.msg == "Mentira":
                    self.grade.cores_quadrados[rows][self.coluna_atual] = (209, 0, 0)
                self.mostrando_carta = False
                self.msg_imagem = None
                self.grade.draw_grid()
                pygame.display.flip()
                break
