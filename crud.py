from sqlalchemy.orm import Session
import schemas
import models


# Operações CRUD para Produtor
def get_produtor(db: Session, produtor_id: int):
    return db.query(models.Produtor).filter(models.Produtor.id_produtor == produtor_id).first()

def get_produtores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Produtor).offset(skip).limit(limit).all()

def create_produtor(db: Session, produtor: schemas.ProdutorCreate):
    db_produtor = models.Produtor(**produtor.dict())
    db.add(db_produtor)
    db.commit()
    db.refresh(db_produtor)
    return db_produtor

# Operações CRUD para Agricultor
def create_agricultor(db: Session, agricultor: schemas.AgricultorCreate):
    # Primeiro cria o produtor
    db_produtor = models.Produtor(
        nome=agricultor.nome,
        endereco=agricultor.endereco,
        tipo='agricultor'
    )
    db.add(db_produtor)
    db.commit()
    db.refresh(db_produtor)
    
    # Depois cria o agricultor
    db_agricultor = models.Agricultor(
        id_produtor=db_produtor.id_produtor,
        nome=agricultor.nome,
        rg=agricultor.rg,
        cpf=agricultor.cpf,
        exp_mercado=agricultor.exp_mercado,
        data_nascimento=agricultor.data_nascimento,
        telefone=agricultor.telefone
    )
    db.add(db_agricultor)
    db.commit()
    db.refresh(db_agricultor)
    
    return db_produtor

# Operações CRUD para Parceria
def create_parceria(db: Session, parceria: schemas.ParceriaCreate):
    db_parceria = models.Parceria(**parceria.dict())
    db.add(db_parceria)
    db.commit()
    db.refresh(db_parceria)
    return db_parceria

def get_parcerias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Parceria).offset(skip).limit(limit).all()

# Operações para visões complexas
def get_resumo_parcerias(db: Session):
    return db.execute("SELECT * FROM resumo_parcerias").fetchall()

def get_analise_recursos(db: Session):
    return db.execute("SELECT * FROM analise_recursos").fetchall()

# Operações CRUD para Funcionario
def update_funcionario_setor(db: Session, funcionario_id: int, novo_setor: str):
    db_funcionario = db.query(models.Funcionario).filter(models.Funcionario.id_func == funcionario_id).first()
    if not db_funcionario:
        return None
    db_funcionario.setor = novo_setor
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario

# Operações CRUD para Empresa
def delete_empresa(db: Session, empresa_id: int):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()
    if not db_empresa:
        return None
    db.delete(db_empresa)
    db.commit()
    return db_empresa