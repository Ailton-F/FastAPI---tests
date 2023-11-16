from fastapi import APIRouter

router = APIRouter(prefix="/usuario")


@router.get("/")
def list_usuario() -> list[dict]:
    return [
        {"1": "Karol"},
        {"2": "Ailton"}
    ]
