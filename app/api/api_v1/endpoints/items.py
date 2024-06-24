from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_items():
    return [{"item_id": "item1"}, {"item_id": "item2"}]
