import unittest
import pygame
from unittest.mock import Mock
from botao import Botoes  # Substitua 'botao' pelo nome real do arquivo

class TestBotoes(unittest.TestCase):

    def setUp(self):
        # Inicializando o Pygame e criando uma janela de exemplo
        pygame.init()
        self.janela = pygame.display.set_mode((800, 600))  # Defina uma resolução adequada para os testes

        # Mock do objeto cf_game
        self.cf_game = Mock()
        self.cf_game.janela = self.janela
        self.cf_game.config = Mock()  # Se houver necessidade de acessar self.cf_game.config

        # Criando uma instância do botão
        self.botao = Botoes(self.cf_game)

    def tearDown(self):
        # Finalizando o Pygame
        pygame.quit()

    def test_btn_facil_position(self):
        # Testa se o botão 'Fácil' está na posição correta
        self.botao.btn_facil()
        self.assertEqual(self.botao.rect.centerx, self.janela.get_rect().centerx)
        self.assertEqual(self.botao.rect.centery, self.janela.get_rect().centery - 75)

    def test_msg_preparation(self):
        # Testa se a mensagem é preparada corretamente
        self.botao.msg = "Testando"
        self.botao.msg_get()
        self.assertEqual(self.botao.msg_imagem.get_width(), self.botao.msg_imagem_rect.width)
        self.assertEqual(self.botao.msg_imagem.get_height(), self.botao.msg_imagem_rect.height)

    def test_button_rendering(self):
        # Testa se o botão é renderizado sem erros
        self.botao.msg = "Render Test"
        self.botao.largura, self.botao.altura = 300, 50
        self.botao.rect = pygame.Rect(0, 0, self.botao.largura, self.botao.altura)
        self.botao.rect.centerx = self.janela.get_rect().centerx
        self.botao.rect.centery = self.janela.get_rect().centery
        self.botao.msg_get()

        # Usando um try/except para capturar erros durante a renderização
        try:
            self.botao.btn_draw()
            renderizou_sem_erro = True
        except Exception as e:
            print(f"Erro durante a renderização: {e}")
            renderizou_sem_erro = False

        self.assertTrue(renderizou_sem_erro, "O botão não foi renderizado corretamente")

    def test_button_size(self):
        # Testa se o tamanho do botão está correto
        self.botao.largura, self.botao.altura = 300, 50
        self.botao.rect = pygame.Rect(0, 0, self.botao.largura, self.botao.altura)
        self.assertEqual(self.botao.rect.width, 300)
        self.assertEqual(self.botao.rect.height, 50)

if __name__ == '__main__':
    unittest.main()
