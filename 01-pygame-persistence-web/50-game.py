# https://www.pygame.org/docs/tut/newbieguide.html

import pygame

# carregar informações de armazenamento
from backend.geral.config import *
from backend.modelo.jogador import Jogador

# Inicialização do Pygame
pygame.init()

# Configurações da tela
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo de Damas")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Variáveis do tabuleiro
board_size = 8
tile_size = width // board_size

# Criação do tabuleiro
board = [[None for _ in range(board_size)] for _ in range(board_size)]

# Preenche o tabuleiro com peças iniciais
for row in range(board_size):
    for col in range(board_size):
        if (row + col) % 2 == 1:
            if row < 3:
                board[row][col] = "peça_preta"
            elif row > 4:
                board[row][col] = "peça_branca"

# Função para desenhar o tabuleiro
def draw_board():
    for row in range(board_size):
        for col in range(board_size):
            color = white if (row + col) % 2 == 0 else black
            pygame.draw.rect(screen, color, (col * tile_size, row * tile_size, tile_size, tile_size))

# Função para desenhar as peças
def draw_pieces():
    for row in range(board_size):
        for col in range(board_size):
            piece = board[row][col]
            if piece == "peça_preta":
                pygame.draw.circle(screen, black, (col * tile_size + tile_size // 2, row * tile_size + tile_size // 2), tile_size // 3)
            elif piece == "peça_branca":
                pygame.draw.circle(screen, white, (col * tile_size + tile_size // 2, row * tile_size + tile_size // 2), tile_size // 3)

# Variáveis para controle de turno e seleção de peça
current_turn = "peça_branca"
selected_piece = None

# Função para atualizar o tabuleiro com os movimentos
def update_board(row, col):
    board[row][col] = selected_piece
    board[selected_piece_row][selected_piece_col] = None

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clique esquerdo do mouse
            col = event.pos[0] // tile_size
            row = event.pos[1] // tile_size
            piece = board[row][col]

            if piece == selected_piece:
                selected_piece = None
            elif selected_piece is None:
                selected_piece = piece
                selected_piece_row = row
                selected_piece_col = col
            elif piece is None and selected_piece is not None:
                update_board(row, col)
                selected_piece = None
                current_turn = "peça_branca" if current_turn == "peça_preta" else "peça_preta"

    screen.fill(black)
    draw_board()
    draw_pieces()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
