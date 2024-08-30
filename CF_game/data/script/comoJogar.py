import pygame.font

class Como_Jogar:

    def __init__(self, cf_game):
        self.cf_game = cf_game
        self.janela = cf_game.janela
        self.estado_jogo = cf_game.estado_jogo
        self.config = self.cf_game.config
        self.font = pygame.font.SysFont(None, 38) 
        self.msg = (
            "Bem-vindo ao Chicken Flag!\n"
            "O objetivo do jogo é ajudar uma galinha a chegar ao seu país de destino, "
            "aprendendo geografia e geopolítica de forma divertida.\n\n"
            "### Como jogar\n"
            "Quando o jogo começa, o nome do país de destino aparece no topo da tela. A galinha deve ser movida "
            "pelas setas do teclado em uma linha, a menos que a tecla espaço seja pressionada, exibindo uma dica. "
            "Você deve responder à dica corretamente para avançar. A galinha só pode se mover verticalmente após "
            "responder a uma dica.\n\n"
            "### Teclas usadas\n"
            "- **Setas do teclado**: Movimentam a galinha na linha.\n"
            "- **Tecla Espaço**: Exibe uma dica sobre o país de destino.\n"
            "- **Tecla Q**: Confirma a saída do jogo.\n"
            "- **Tecla S**: Confirma a saída do jogo quando perguntado.\n"
            "- **Tecla N**: Cancela a saída do jogo quando perguntado.\n\n"
            "### Sistema de pontuação\n"
            "A pontuação é calculada com base nas suas respostas e no tempo de jogo:\n"
            "- **Resposta correta de dica**: +50 pontos\n"
            "- **Resposta errada de dica**: -30 pontos\n"
            "- **Tempo de jogo**:\n"
            "  - Menos de 1 minuto: +50 pontos\n"
            "  - Menos de 2 minutos: +30 pontos\n"
            "  - Mais de 2 minutos: +10 pontos\n"
            "- **Dificuldade**:\n"
            "  - Fácil: +50 pontos\n"
            "  - Médio: +100 pontos\n"
            "  - Difícil: +150 pontos\n\n"
            "- **Resultado**:\n"
            "  -Vitória: +200 pontos\n"
            "  -Derrota: -200 pontos\n"
            "Divirta-se jogando Chicken Flag e aprenda sobre o mundo enquanto ajuda a galinha a chegar ao seu destino!\n"
            "LEMBRE-SE: PARA SAIR CLIK Q."
        )
        self.cor_texto = (255, 255, 255)
        self.cor = self.config.bg_color
        self.mostrar_instrucoes = False
        self.scroll_offset = 0
        self.barra_cor = (100, 100, 100)
        self.barra_largura = 10
        self.barra_rect = pygame.Rect(self.config.janela_largura - self.barra_largura, 0, self.barra_largura, 0)
        self.barra_drag = False
        self.barra_pos_inicial = 0

    def _quebrar_texto(self, texto, largura_max):
        paragrafos = texto.split('\n')  # Dividindo o texto em parágrafos
        linhas = []
        for paragrafo in paragrafos:
            palavras = paragrafo.split(' ')
            linha_atual = []
            largura_atual = 0

            for palavra in palavras:
                if '\n' in palavra:
                    sub_palavras = palavra.split('\n')
                    for sub_palavra in sub_palavras:
                        largura_sub_palavra, _ = self.font.size(sub_palavra + ' ')
                        if largura_atual + largura_sub_palavra <= largura_max:
                            linha_atual.append(sub_palavra)
                            largura_atual += largura_sub_palavra
                        else:
                            linhas.append(' '.join(linha_atual))
                            linha_atual = [sub_palavra]
                            largura_atual = largura_sub_palavra
                else:
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
            linhas.append('')  # Adicionando uma linha em branco entre os parágrafos

        return linhas

    def _info(self, x, y):
        if self.msg:
            linhas = self._quebrar_texto(self.msg, self.config.janela_largura - 20)
            y_offset = y + 20 - self.scroll_offset  # Distância do topo da carta

            for linha in linhas:
                if linha.strip():  # Ignora linhas em branco
                    linha_imagem = self.font.render(linha, True, self.cor_texto, self.cor)
                    linha_imagem_rect = linha_imagem.get_rect()
                    linha_imagem_rect.x = x + 10  # Distância das bordas laterais
                    linha_imagem_rect.y = y_offset
                    self.janela.blit(linha_imagem, linha_imagem_rect)
                    y_offset += linha_imagem_rect.height + 5  # Espaçamento entre linhas

    def _desenhar_barra(self):
        # Calcula a altura da barra de rolagem
        altura_total = len(self.msg.split('\n')) * (self.font.get_linesize() + 5)
        altura_visivel = self.config.janela_altura - 20
        proporcao = altura_visivel / altura_total
        barra_altura = altura_visivel * proporcao

        # Atualiza a posição e a altura da barra de rolagem
        self.barra_rect.height = barra_altura
        self.barra_rect.y = (self.scroll_offset / (altura_total - altura_visivel)) * (altura_visivel - barra_altura)

        # Desenha a barra de rolagem
        pygame.draw.rect(self.janela, self.barra_cor, self.barra_rect)

    def draw_info(self):
        if self.mostrar_instrucoes:  # Verifica se as instruções devem ser exibidas
            self._info(10, 10)  # Desenha as instruções na tela
            self._desenhar_barra()

    def _scroll(self, delta):
        # Rolagem para cima ou para baixo
        self.scroll_offset += delta
        self.scroll_offset = max(0, min(self.scroll_offset, len(self.msg.split('\n')) * (
                    self.font.get_linesize() + 15) - self.config.janela_altura))
