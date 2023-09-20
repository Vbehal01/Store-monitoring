from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import model, crud
from database import engine, SessionLocal

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/insert-store-status/")
def store_status(db: Session = Depends(get_db)):
    crud.insert_store_status(db)
    return {"message": "Store status data inserted successfully."}

@app.post("/insert-menu-hour/")
def menu_hour(db: Session = Depends(get_db)):
    crud.insert_menu_hours(db)
    return {"message": "menu hour data inserted successfully."}

@app.post("/insert-bq_results/")
def bq_results(db: Session = Depends(get_db)):
    crud.insert_bq_results(db)
    return {"message": "bq results data inserted successfully."}
