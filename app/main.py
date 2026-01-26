from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Expertly AI Demos")

@app.get("/health")
def health():
    return JSONResponse({"status": "healthy"})

app.mount("/", StaticFiles(directory="static", html=True), name="static")
