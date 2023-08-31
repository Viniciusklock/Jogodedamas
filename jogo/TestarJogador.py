from config import *
from jogador import Jogador

    
j1 = Jogador(nome = "Nick Hack", movimentos="15")

db.session.add(j1)
db.session.commit()

print(j1)