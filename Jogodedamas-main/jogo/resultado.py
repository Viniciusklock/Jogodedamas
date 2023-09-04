from config import *

class Resultado(db.Model):
    # atributo auto-gerado
    id = db.Column(db.Integer, primary_key=True)
    # posições do jogo
    # nome do jogador
    nome_ganhador = db.Column(db.Text)

    def __str__(self):
        return f'{self.nome_ganhador} você ganhou! '
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome ganhador": self.nome_ganhador
        }