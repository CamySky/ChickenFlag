import sys, os
import time
import pygame
from data.script.config import Config
from data.script.chicken import Chicken
from data.script.grade import Grade
from data.script.cartas import Cartas
from data.script.dicas import Dicas
from data.script.escritas import Escrevendo
from data.script.final import Finalizando
from data.script.comoJogar import Como_Jogar

dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

class ChickenFlag:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.janela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Chicken Flag")

        self.prin_mov = True
        self.space_pressed = True

        self.estado_jogo = 'inicio'

        self.tempo_inicial = time.time()
        self.tempo_pausado_total = 0
        self.tempo_pausado_inicial = 0

        self.config = Config(self)
        self.chicken = Chicken(self)
        self.dicas = Dicas(self)
        self.grade = Grade(self)
        self.finalizando = Finalizando(self)
        self.cartas = Cartas(self)
        self.escrevendo = Escrevendo(self)
        self.como_jogar = Como_Jogar(self)

        self.font = pygame.font.SysFont(None, 48)
        self.confirmar_saida = False

    def principal(self):
        while True:
            self._check_events()
            if self.estado_jogo == 'inicio':
                self._update_principal()
            elif self.estado_jogo == 'jogando' or self.estado_jogo == 'pausado':
                self._update_jogo()
            elif self.estado_jogo == 'final':
                self._update_final()
            elif self.estado_jogo == 'instrucoes':
                self._update_instrucoes()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_MOUSEBUTTONDOWN(pygame.mouse.get_pos(), event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.como_jogar.barra_drag = False
            elif event.type == pygame.MOUSEMOTION:
                if self.como_jogar.barra_drag:
                    delta_y = event.pos[1] - self.como_jogar.barra_pos_inicial
                    self.como_jogar.barra_pos_inicial = event.pos[1]
                    self.como_jogar._scroll(-delta_y)
                elif event.type == pygame.VIDEORESIZE:
                    self._resize_window(event.w, event.h)


    def _check_MOUSEBUTTONDOWN(self, mouse_pos, event):
        if self.cartas.mostrando_carta:
            self.cartas.check_click_botao(mouse_pos, self.chicken.rows)
        elif self.estado_jogo == 'final':
            if self.config.voltar_menu.rect.collidepoint(mouse_pos):
                self.estado_jogo = 'inicio'
        elif self.config.botao_pausa.rect.collidepoint(mouse_pos) or self.config.botao_despausa.rect.collidepoint(mouse_pos):
            if self.estado_jogo == 'jogando':
                self.estado_jogo = 'pausado'
                self.tempo_pausado_inicial = time.time()
            elif self.estado_jogo == 'pausado':
                self.estado_jogo = 'jogando'
                self.tempo_pausado_total += time.time() - self.tempo_pausado_inicial
        elif self.config.voltar_menu.rect.collidepoint(mouse_pos) or self.config.voltar_menu_jogo.rect.collidepoint(mouse_pos):
            self.estado_jogo = 'inicio'
        else:
            self._check_play(mouse_pos)
            if event.button == 4:
                self.como_jogar._scroll(-50)  # Rolar para cima
            elif event.button == 5:
                self.como_jogar._scroll(50)  # Rolar para baixo
            elif self.como_jogar.barra_rect.collidepoint(event.pos):
                self.como_jogar.barra_drag = True
                self.como_jogar.barra_pos_inicial = event.pos[1]

    def _check_keydown(self, event):
        if self.confirmar_saida:
            if event.key == pygame.K_s:
                sys.exit()
            elif event.key == pygame.K_n:
                self.confirmar_saida = False
        if event.key == pygame.K_RIGHT and not self.cartas.mostrando_carta:
            self.chicken.mover(0, 1)
        elif event.key == pygame.K_LEFT and not self.cartas.mostrando_carta:
            self.chicken.mover(0, -1)
        elif event.key == pygame.K_UP and not self.cartas.mostrando_carta and (self.space_pressed or self.prin_mov):
            self.chicken.mover(-1, 0)
            self.prin_mov = False
            self.space_pressed = False
            if self.chicken.rows == 0:
                self.finalizando.pontos_finais()
                self.estado_jogo = 'final'
        elif event.key == pygame.K_q:
            self.confirmar_saida = True
        elif event.key == pygame.K_SPACE and not self.cartas.mostrando_carta and self.estado_jogo == 'jogando':
            if self.grade.cores_quadrados[self.chicken.rows][self.chicken.cols] == self.config.grade_cor:
                self.space_pressed = True
                self.cartas._draw_carta(self.chicken.cols)

    def _check_play(self, mouse_pos):
        if self.config.facil.rect.collidepoint(mouse_pos) and self.estado_jogo == 'inicio':
            self.config.set_dificuldade(7, 4)
            self.grade.update_dimensions()
            self.dicas._atualizar_pais(4)
            self.finalizando.pontos_por_dificuldade("facil")
            self.estado_jogo = 'jogando'
            self.tempo_inicial = time.time()
            if self.prin_mov == False:
                self.prin_mov = True
                self.__init__()
        elif self.config.medio.rect.collidepoint(mouse_pos) and self.estado_jogo == 'inicio':
            self.config.set_dificuldade(6, 6)
            self.grade.update_dimensions()
            self.dicas._atualizar_pais(6)
            self.finalizando.pontos_por_dificuldade("medio")
            self.estado_jogo = 'jogando'
            self.tempo_inicial = time.time()
            if self.prin_mov == False:
                self.prin_mov = True
                self.__init__()
        elif self.config.dificil.rect.collidepoint(mouse_pos) and self.estado_jogo == 'inicio':
            self.config.set_dificuldade(4, 8)
            self.grade.update_dimensions()
            self.dicas._atualizar_pais(8)
            self.finalizando.pontos_por_dificuldade("dificil")
            self.estado_jogo = 'jogando'
            self.tempo_inicial = time.time()
            if self.prin_mov == False:
                self.prin_mov = True
                self.__init__()
        elif self.config.comojogar.rect.collidepoint(mouse_pos) and self.estado_jogo == 'inicio':
            self.estado_jogo = 'instrucoes'
            self.como_jogar.mostrar_instrucoes = True

    def _update_principal(self):
        self.como_jogar.mostrar_instrucoes = False
        self.janela.fill(self.config.bg_color)
        self.escrevendo.escrever("Chicken Flag", self.config.janela_largura)
        self.config.facil.draw_botao()
        self.config.medio.draw_botao()
        self.config.dificil.draw_botao()
        self.config.comojogar.draw_botao()
        if self.confirmar_saida:
            self._draw_confirm_exit()
        pygame.display.flip()

    def _update_instrucoes(self):
        self.janela.fill(self.config.bg_color)
        self.como_jogar.draw_info()
        self.config.voltar_menu.draw_botao()
        if self.confirmar_saida:
            self._draw_confirm_exit()
        pygame.display.flip()

    def _update_jogo(self):
        self.janela.fill(self.config.bg_color)
        self.config.voltar_menu_jogo.draw_botao()
        self._draw_timer()
        if self.estado_jogo == 'pausado':
            self._draw_pause_screen()
            self.config.botao_despausa.draw_botao()
        else:
            self.grade.update()
            self.chicken.blitme()
            self.config.botao_pausa.draw_botao()
            self.dicas.mostrar_pais.draw_botao()
            if self.cartas.mostrando_carta:
                self.cartas.draw()
            if self.confirmar_saida:
                self._draw_confirm_exit()
        pygame.display.flip()

    def _update_final(self):
        self.janela.fill(self.config.bg_color)
        self.finalizando.draw_pontos(self.janela, self.font)
        self.finalizando.resultado()
        self.config.voltar_menu.draw_botao()
        if self.confirmar_saida:
            self._draw_confirm_exit()
        pygame.display.flip()

    def _resize_window(self, width, height):
        self.janela = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.config.janela_largura = width - self.config.margem
        self.config.janela_altura = height - self.config.margem
        self.config._recalcular_tamanhos()
        self.grade.update_dimensions()

    def _draw_pause_screen(self):
        # Desenhar tela de pausa
        largura_fundo = self.config.janela_largura
        altura_fundo = self.config.janela_altura
        x_fundo = (self.config.janela_largura - largura_fundo) // 2
        y_fundo = (self.config.janela_altura - altura_fundo) // 2

        pygame.draw.rect(self.janela, (0, 0, 0), (x_fundo, y_fundo, largura_fundo, altura_fundo))
        pause_text = "Jogo pausado..."
        font = pygame.font.SysFont(None, 48)
        pause_imagem = font.render(pause_text, True, (255, 255, 255))
        pause_rect = pause_imagem.get_rect(center=self.janela.get_rect().center)

        pause_rect.center = (x_fundo + largura_fundo // 2, y_fundo + altura_fundo // 2)
        self.janela.blit(pause_imagem, pause_rect)

    def _draw_timer(self):
        if self.tempo_inicial:
            if self.estado_jogo != 'pausado':
                self.tempo_decorrido = time.time() - self.tempo_inicial - self.tempo_pausado_total
            else:
                self.tempo_decorrido = self.tempo_pausado_inicial - self.tempo_inicial - self.tempo_pausado_total

            minutos = int(self.tempo_decorrido // 60)
            segundos = int(self.tempo_decorrido % 60)
            timer_text = f"Tempo: {minutos:02}:{segundos:02}"
            font = pygame.font.SysFont(None, 48)
            timer_imagem = font.render(timer_text, True, (255, 255, 255))
            self.janela.blit(timer_imagem, (10, 10))

    def _draw_confirm_exit(self):
        largura_fundo = 600
        altura_fundo = 200
        x_fundo = (self.config.janela_largura - largura_fundo) // 2
        y_fundo = (self.config.janela_altura - altura_fundo) // 2

        pygame.draw.rect(self.janela, (0, 0, 0), (x_fundo, y_fundo, largura_fundo, altura_fundo))
        confirm_text = "Confirmar saída? (S)im (N)ão"
        font = pygame.font.SysFont(None, 48)
        confirm_imagem = font.render(confirm_text, True, (255, 255, 255))
        confirm_rect = confirm_imagem.get_rect(center=self.janela.get_rect().center)

        confirm_rect.center = (x_fundo + largura_fundo // 2, y_fundo + altura_fundo // 2)
        self.janela.blit(confirm_imagem, confirm_rect)


if __name__ == '__main__':
    cf = ChickenFlag()
    cf.principal()

