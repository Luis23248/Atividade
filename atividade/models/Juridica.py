from models.Pessoa import Pessoa
from models.Endereco import Endereco





class Juridica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str):
        
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual