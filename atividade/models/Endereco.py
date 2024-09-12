from models.enums.Unidade_Federativa import Unidade_Federativa




class Endereco:

    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: Unidade_Federativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf