from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog.database import get_db
from blog.functions import user
from blog.schemas import User, ShowUser

router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
