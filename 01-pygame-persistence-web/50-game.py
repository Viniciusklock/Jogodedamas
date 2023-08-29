# https://www.pygame.org/docs/tut/newbieguide.html

import pygame

# carregar informações de armazenamento
from backend.geral.config import *
from backend.modelo.jogador import Jogador

# posições iniciais da bola
x = 320
y = 320

# tentar carregar x e y
with app.app_context():
    try:
        obj = db.session.get(Jogador, 1) # carrega o jogador
        x = obj.x
        y = obj.y
    except Exception as e:
        print("Não foi possível carregar informações: "+str(e))

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()


# criar/carregar fonte
font = pygame.font.Font('freesansbold.ttf', 32)
# criar um texto
text = font.render('Pressione Q para finalizar', True, (100, 100, 100), (11, 11, 11))
# definir retângulo no qual vai aparecer o texto
# pega o do próprio texto
text_rect = text.get_rect()

running = True
while running:
    
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit     

    # Do logical updates here.
    # ...

    # outra forma de capturar eventos de teclado :-)
    # esta verificação fica FORA da seção sugerida para processar eventos :-/
    # https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    if keys[pygame.K_q]:
        running = False

    screen.fill("purple")  # Fill the display with a solid color

    # coloca o texto na tela
    screen.blit(text, text_rect)

    pygame.draw.circle(screen, (10, 10, 10), [x, y], 15, 5)

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)

    # salvar os dados
    with app.app_context():
        obj = db.session.get(Jogador, 1) # carrega o jogador
        obj.x = x # atualiza coordenadas
        obj.y = y
        db.session.commit() # salva!

print("Jogo encerrado e informações salvas")