import sys
import os
import time
import pygame
from data.script.config import Config
from data.script.chicken import Chicken
from data.script.grade import Grade
from data.script.cartas import Cartas
from data.script.botao import Botoes
from data.script.dicas import Dicas
from data.script.escritas import Escrevendo
from data.script.final import Finalizando
from data.script.comoJogar import Como_Jogar

#Para a criação do .exe
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)


class ChickenFlag:

    #Iniciando os principais atributos e depêndencias do jogo
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.clock = pygame.time.Clock()

        self.janela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Chicken Flag")

        self.prin_mov = True
        self.press_espaco = True
        self.confirmar_saida = False
        self.estado_jogo = 'inicio'

        self.tempo_inicial = time.time()
        self.tempo_pausado_total = 0
        self.tempo_pausado_inicial = 0

        self.config = Config(self)
        self.botoes = Botoes(self)
        self.chicken = Chicken(self)
        self.escrevendo = Escrevendo(self)
        self.dicas = Dicas(self)
        self.grade = Grade(self)
        self.finalizando = Finalizando(self)
        self.cartas = Cartas(self)
       
        self.como_jogar = Como_Jogar(self)

    #Controle de Status do jogo, auxilia qual tela mostrar
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

    #Checa quaisquer evento (clicks) do usuário
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

    #Trata dos eventos na tela inicial
    def _check_play(self, mouse_pos):
        if self.botoes.btn_facil().collidepoint(mouse_pos) and self.estado_jogo == 'inicio':
            self.config.set_dificuldade(7, 4)
            self.grade.update_dimensions()
            self.dicas._atualizar_pais(4)
            self.finalizando.pontos_por_dificuldade("facil")
            self.estado_jogo = 'jogando'
            self.tempo_inicial = time.time()
            if self.prin_mov == False:
                self.prin_mov = True
                self.__init__()
        elif self.botoes.btn_medio().collidepoint(mouse_pos) and self.estado_jogo == 'inicio':
            self.config.set_dificuldade(6, 6)
            self.grade.update_dimensions()
            self.dicas._atualizar_pais(6)
            self.finalizando.pontos_por_dificuldade("medio")
            self.estado_jogo = 'jogando'
            self.tempo_inicial = time.time()
            if self.prin_mov == False:
                self.prin_mov = True
                self.__init__()
        elif self.botoes.btn_dificil().collidepoint(mouse_pos) and self.estado_jogo == 'inicio':
            self.config.set_dificuldade(4, 8)
            self.grade.update_dimensions()
            self.dicas._atualizar_pais(8)
            self.finalizando.pontos_por_dificuldade("dificil")
            self.estado_jogo = 'jogando'
            self.tempo_inicial = time.time()
            if self.prin_mov == False:
                self.prin_mov = True
                self.__init__()
        elif self.botoes.btn_comoJogar().collidepoint(mouse_pos) and self.estado_jogo == 'inicio':
            self.estado_jogo = 'instrucoes'
            self.como_jogar.mostrar_instrucoes = True

    #Trata dos eventos causados pelo mouse
    def _check_MOUSEBUTTONDOWN(self, mouse_pos, event):
        if self.cartas.mostrando_carta:
            self.cartas.check_click_botao(mouse_pos, self.chicken.rows)
        elif self.estado_jogo == 'final':
            if self.botoes.btn_menuBack().collidepoint(mouse_pos):
                self.estado_jogo = 'inicio'
        elif self.botoes.btn_pausar().collidepoint(mouse_pos) or self.botoes.btn_despausar().collidepoint(mouse_pos):
            if self.estado_jogo == 'jogando':
                self.estado_jogo = 'pausado'
                self.tempo_pausado_inicial = time.time()
            elif self.estado_jogo == 'pausado':
                self.estado_jogo = 'jogando'
                self.tempo_pausado_total += time.time() - self.tempo_pausado_inicial
        elif self.botoes.btn_menu().collidepoint(mouse_pos) or self.botoes.btn_menuBack().collidepoint(mouse_pos):
            self.estado_jogo = 'inicio'
        else:
            self._check_play(mouse_pos)
            if event.button == 4:
                self.como_jogar._scroll(-50) 
            elif event.button == 5:
                self.como_jogar._scroll(50) 
            elif self.como_jogar.barra_rect.collidepoint(event.pos):
                self.como_jogar.barra_drag = True
                self.como_jogar.barra_pos_inicial = event.pos[1]

    #Trata dos eventos do teclado
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
        elif event.key == pygame.K_UP and not self.cartas.mostrando_carta and (self.press_espaco or self.prin_mov):
            self.chicken.mover(-1, 0)
            self.prin_mov = False
            self.press_espaco = False
            if self.chicken.rows == 0:
                self.finalizando.pontos_finais()
                self.estado_jogo = 'final'
        elif event.key == pygame.K_q:
            self.confirmar_saida = True
        elif event.key == pygame.K_SPACE and not self.cartas.mostrando_carta and self.estado_jogo == 'jogando':
            if self.grade.cores_quadrados[self.chicken.rows][self.chicken.cols] == self.config.grade_cor:
                self.press_espaco = True
                self.cartas._draw_carta(self.chicken.cols)

    #Update de acordo com cada estado do jogo
    def _update_principal(self):
        self.como_jogar.mostrar_instrucoes = False
        self.janela.fill(self.config.bg_color)
        self.escrevendo.escrever_centro_acima("Chicken Flag", 80)
        self.botoes.btn_facil()
        self.botoes.btn_medio()
        self.botoes.btn_dificil()
        self.botoes.btn_comoJogar()
        if self.confirmar_saida:
            self.escrevendo.escerver_segundo_plano("Confirmar saída? [S]im [N]ão")
        pygame.display.flip()

    def _update_instrucoes(self):
        self.janela.fill(self.config.bg_color)
        self.como_jogar.draw_info()
        self.botoes.btn_menuBack()
        if self.confirmar_saida:
            self.escrevendo.escerver_segundo_plano("Confirmar saída? [S]im [N]ão")
        pygame.display.flip()

    def _update_jogo(self):
        self.janela.fill(self.config.bg_color)
        self.botoes.btn_menuBack()
        self.calcular_tempo()
        if self.estado_jogo == 'pausado':
            self.escrevendo.escerver_segundo_plano("Jogo pausado...")
            self.botoes.btn_despausar()
        else:
            self.grade.update()
            self.chicken.blitme()
            self.botoes.btn_pausar()
            self.dicas.pais_draw()
            if self.cartas.mostrando_carta:
                self.cartas.draw()
            if self.confirmar_saida:
                self.escrevendo.escerver_segundo_plano("Confirmar saída? [S]im [N]ão")
        pygame.display.flip()

    def _update_final(self):
        self.janela.fill(self.config.bg_color)
        self.escrevendo.escrever_canto_dir_acima(f"Pontos: {self.finalizando.pontos}")
        self.finalizando.resultado()
        self.botoes.btn_menuBack()
        if self.confirmar_saida:
            self.escrevendo.escerver_segundo_plano("Confirmar saída? [S]im [N]ão")
        pygame.display.flip()

    #Redefine a grade a cada interação
    def _resize_window(self, width, height):
        self.janela = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.config.janela_largura = width - self.config.margem
        self.config.janela_altura = height - self.config.margem
        self.config._recalcular_tamanhos()
        self.grade.update_dimensions()

    def calcular_tempo(self):
        if self.tempo_inicial:
            if self.estado_jogo != 'pausado':
                self.tempo_decorrido = time.time() - self.tempo_inicial - \
                    self.tempo_pausado_total
            else:
                self.tempo_decorrido = self.tempo_pausado_inicial - \
                    self.tempo_inicial - self.tempo_pausado_total

            minutos = int(self.tempo_decorrido // 60)
            segundos = int(self.tempo_decorrido % 60)

            self.escrevendo.escrever_canto_dir_acima(f"Tempo: {minutos:02}:{segundos:02}")
           
#Ponto de partida do jogo, inicia no metodo "pricipal"           
if __name__ == '__main__':
    cf = ChickenFlag()
    cf.principal()