from backend.geral.config import *
from backend.modelo.jogador import Jogador

def run():
    print("TESTE DE JOGADOR")
    
    j1 = Jogador(nome = "Nick Hack", x = 300, y = 100)
    db.session.add(j1)
    db.session.commit()
    print(j1)
    print(j1.json())