from utils.db import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cor1 = db.Column(db.String(100))
    modelo1 = db.Column(db.String(100))
    cor2 = db.Column(db.String(100))
    modelo2 = db.Column(db.String(100))
    cor3 = db.Column(db.String(100))
    modelo3 = db.Column(db.String(100))
    
    def __init__(self, nome,cor1,modelo1,cor2,modelo2,cor3,modelo3):
        self.nome = nome
        self.cor1 = cor1
        self.modelo1 = modelo1
        self.cor2 = cor2
        self.modelo2 = modelo2
        self.cor3 = cor3
        self.modelo3 = modelo3