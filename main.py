from fastapi import FastAPI, Depends, HTTPException
from typing import List
import schemas
import models
import crud
from db import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/produtores/agricultor/", response_model=schemas.Produtor)
def create_agricultor(agricultor: schemas.AgricultorCreate, db: Session = Depends(get_db)):
    return crud.create_agricultor(db=db, agricultor=agricultor)

@app.get("/produtores/", response_model=List[schemas.Produtor])
def read_produtores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    produtores = crud.get_produtores(db, skip=skip, limit=limit)
    return produtores

@app.post("/parcerias/", response_model=schemas.Parceria)
def create_parceria(parceria: schemas.ParceriaCreate, db: Session = Depends(get_db)):
    return crud.create_parceria(db=db, parceria=parceria)

@app.get("/parcerias/resumo/", response_model=List[schemas.ResumoParcerias])
def read_resumo_parcerias(db: Session = Depends(get_db)):
    parcerias = crud.get_resumo_parcerias(db)
    return parcerias

@app.get("/recursos/analise/", response_model=List[schemas.AnaliseRecursos])
def read_analise_recursos(db: Session = Depends(get_db)):
    recursos = crud.get_analise_recursos(db)
    return recursos

@app.put("/funcionarios/{funcionario_id}/setor/", response_model=schemas.Funcionario)
def update_funcionario_setor(
    funcionario_id: int, 
    setor: str, 
    db: Session = Depends(get_db)
):
    db_funcionario = crud.update_funcionario_setor(db, funcionario_id=funcionario_id, novo_setor=setor)
    if db_funcionario is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return db_funcionario

@app.delete("/empresas/{empresa_id}/", response_model=schemas.Empresa)
def delete_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = crud.delete_empresa(db, empresa_id=empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return {"message": "Empresa deletada com sucesso"}

@app.get("/")
def read_root():
    return {"message": "Sistema de Gerenciamento de Cooperativa"}