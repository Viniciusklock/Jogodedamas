from backend.geral.config import *

class Jogador(db.Model):
    # atributo auto-gerado
    id = db.Column(db.Integer, primary_key=True)
    # posições do jogo
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    # nome do jogador
    nome = db.Column(db.Text)

    def __str__(self):
        return f'{self.nome} parou em {self.x} e {self.y}'
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "nome": self.nome
        }