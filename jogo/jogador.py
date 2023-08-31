from config import *

class Jogador(db.Model):
    # atributo auto-gerado
    id = db.Column(db.Integer, primary_key=True)
    # posições do jogo
    movimentos = db.Column(db.Integer)
    # nome do jogador
    nome = db.Column(db.Text)

    def __str__(self):
        return f'{self.nome} realizou {self.movimentos} movimentos '
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "movimentos": self.movimentos,
            "nome": self.nome
        }