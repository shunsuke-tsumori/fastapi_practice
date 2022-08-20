from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from blog import models, token
from blog.database import get_db
from blog.hashing import Hash
from blog.schemas import Login

router = APIRouter(
    tags=["Auth"]
)


@router.post("/login")
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
