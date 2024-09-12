from models.Fisica import Fisica
from models.enums.Setor import Setor
from models.Endereco import Endereco
from models.enums.Genero import Genero
from abc import ABC, abstractmethod





class Funcionario(Fisica, ABC):
    def __init__(self, nome: str, telefone:str, email: str, endereco: Endereco, cpf: str, rg: str , data_nascimento: str, genero: Genero, matricula: str, setor: Setor, salario: float):
        super().__init__(nome, telefone, email, endereco, cpf, rg, data_nascimento, genero)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario
    

    @abstractmethod
    def salario_final(self)-> float :
        pass

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nMátricula: {self.matricula}"
                f"\nSetor: {self.setor}"
                f"\nSalário: {self.salario}"
                f"\nSalário final: {self.salario_final()}")               