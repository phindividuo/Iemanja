from fastapi import FastAPI

app = FastAPI(
    title="Iemanjá",
    description="Monitoramento de condições oceânicas da costa Fluminense no Rio de Janeiro",
    version="0.1.0",
)

@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}

@app.get("/")
async def raiz():
    return {"projeto": "Iemanjá", "docs": "/docs"}
