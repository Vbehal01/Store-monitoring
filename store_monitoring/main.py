from fastapi import FastAPI
from sqlalchemy.orm import Session
import model, database

model.Base.metadata.create_all(bind=database.engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
