from models.Pessoa import Pessoa
from models.enums.Genero import Genero
from models.Endereco import Endereco



class Fisica(Pessoa):
    def __init__(self, nome:str, telefone:str, email:str, endereco: Endereco, cpf:str, rg:str, data_nascimento:str, genero: Genero):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.genero = genero

    def __str__(self):
        return (
             
                f"\nCPF: {self.cpf}" 
                f"\nRG: {self.rg}"
                f"\nData de Nascimento: {self.data_nascimento}" 
                f"\nGênero: {self.genero.name}"

        )
        