import uvicorn
import sys
import os

# Adicionar o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    uvicorn.run(
        "src.backend.principal:aplicacao",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )