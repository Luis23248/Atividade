from models.Pessoa import Pessoa
from models.enums.Genero import Genero
from models.Endereco import Endereco
from models.Fisica import Fisica

class Cliente(Fisica):


    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, genero: Genero, protocolo_atendimento: int):
        super().__init__(nome, telefone, email, endereco, cpf, rg, data_nascimento, genero)
        self.protocolo_atendimento = protocolo_atendimento


    def __str__(self):
        return (
            f"{super().__str__()}\nProtocolo de atendimento: {self.protocolo_atendimento}")    