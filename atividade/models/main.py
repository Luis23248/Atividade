
from models.Pessoa import Pessoa
from models.Endereco import Endereco
from models.enums.Unidade_Federativa import Unidade_Federativa
from models.Funcionario import Funcionario
from models.enums.Genero import Genero
from models.enums.Setor import Setor

os.system("cls || clear")
import os



endereco_2 = Endereco("rua c", "151", "Casa", "4844448", "Salvador", Unidade_Federativa.BAHIA)
endereco_1 = Endereco("Rua D", "78", "Casa", "875446", "Salvador", Unidade_Federativa.BAHIA)
pessoa_1 = Pessoa("Roberto", "871854887", "sdwads@hotmail.com",endereco_1 )
funcionario_1 = Funcionario("robson", "44848484", "esadwad@haotyas", endereco_2, "487884848484", "15151484", "17/02/1999", Genero.MASCULINO.value, "1515454545",Setor.SAUDE, 7000 )

print(pessoa_1)