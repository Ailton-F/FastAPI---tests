import uvicorn
from fastapi import FastAPI
from usuario.routers import usuario_router

app = FastAPI()
app.include_router(usuario_router.router)


@app.get('/')
def oi_mundo() -> str:
    return "Hello, world!"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
