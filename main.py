from fastapi import FastAPI
from routers import return_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 
# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Aquí puedes especificar los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Aquí puedes especificar los métodos HTTP permitidos
    allow_headers=["*"],  # Aquí puedes especificar los encabezados HTTP permitidos
)


app.include_router(return_text.router)

@app.get("/")
def read_root():
    return {"Hello": "World from main"}

