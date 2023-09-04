from config import *
from resultado import Resultado

    
j1 = Resultado(nome_ganhador = "Nick Hack")

db.session.add(j1)
db.session.commit()

print(j1)