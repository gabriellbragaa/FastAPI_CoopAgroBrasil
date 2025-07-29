from fastapi import FastAPI, Depends, HTTPException
from typing import List

from crud               import router as  produtor_router
from crud_funcionario   import router as  funcionario_router
from crud_pecuarista    import router as  pecuarista_router
from crud_agricultor    import router as  agricultor_router
from crud_parceria      import router as  parceria_router
from crud_administrador import router as  administrador_router
from crud_client        import router as  client_router
from crud_recurso       import router as  recurso_router
from completo           import router as  completo_router
from crud_empresa       import router as  empresa_router

from models import ProdutorUpdate

app = FastAPI(
    title="CoopAgroBrasil API",
    description="API para gerenciamento de produtores, agricultores, parcerias e recursos na CoopAgroBrasil.",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "API CoopAgro funcionando!"}

app.include_router(produtor_router, prefix="/produtor", tags=["Produtor"])
app.include_router(funcionario_router, prefix="/funcionario", tags=["Funcionário"])
app.include_router(pecuarista_router, prefix="/pecuarista", tags=["Pecuarista"] )
app.include_router(agricultor_router, prefix="/agricultor", tags=["Agricultor"])
app.include_router(parceria_router, prefix="/parceria", tags=["Parceria"])
app.include_router(administrador_router, prefix="/administrador", tags=["Administrador"])
app.include_router(client_router, prefix="/client", tags=["Client"])
app.include_router(recurso_router, prefix="/recurso", tags=["Recurso"])
app.include_router(completo_router, prefix="/completo", tags=["Completo"])
app.include_router(empresa_router, prefix="/empresa", tags=["Empresa"])