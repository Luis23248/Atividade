from models.Fisica import Fisica
from models.enums.Setor import Setor







class Funcionario(Fisica):
    def __init__(self, nome, telefone, email, endereco, cpf, rg, data_nascimento, genero, matricula, setor: Setor, salario):
        super().__init__(nome, telefone, email, endereco, cpf, rg, data_nascimento, genero)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario
    
    def salario_final(self):
        pass