from pydantic import BaseModel
from typing import Optional, List

# Modelos Pydantic para validação de entrada/saída
class ProdutorBase(BaseModel):
    nome: str
    endereco: str

class ProdutorCreate(ProdutorBase):
    tipo: str

class Produtor(ProdutorBase):
    id_produtor: int
    tipo: str
    
    class Config:
        orm_mode = True

class AgricultorCreate(BaseModel):
    nome: str
    rg: str
    cpf: str
    exp_mercado: int
    data_nascimento: str
    telefone: str
    endereco: str

class Agricultor(AgricultorCreate):
    id_produtor: int
    
    class Config:
        orm_mode = True

class PecuaristaBase(BaseModel):
    nome: str
    rg: str
    endereco: str
    cnpj: str
    qualidade_produto: str

class PecuaristaCreate(PecuaristaBase):
    pass

class Pecuarista(PecuaristaBase):
    id_produtor: int
    
    class Config:
        orm_mode = True

class ParceriaBase(BaseModel):
    id_empresa: int
    id_cooperativa: int

class ParceriaCreate(ParceriaBase):
    pass

class Parceria(ParceriaBase):
    class Config:
        orm_mode = True

class FuncionarioBase(BaseModel):
    nome: str
    rg: str
    endereco: str
    setor: str
    id_admin: int

class FuncionarioCreate(FuncionarioBase):
    pass

class Funcionario(FuncionarioBase):
    id_func: int
    
    class Config:
        orm_mode = True

class RecursoBase(BaseModel):
    qualidade: str
    logistica: str
    armazenamento: str
    quantidade: int
    valor_mercado: float
    demandas: str

class RecursoCreate(RecursoBase):
    pass

class Recurso(RecursoBase):
    id_recurso: int
    
    class Config:
        orm_mode = True