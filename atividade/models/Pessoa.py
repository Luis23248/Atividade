from models.enums.Genero import Genero
from models.enums.Setor import Setor
from models.Endereco import Endereco



class Pessoa:

    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco