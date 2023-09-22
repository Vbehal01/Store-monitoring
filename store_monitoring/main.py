from fastapi import Depends, FastAPI, BackgroundTasks
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

# @app.post("/insert-store-status/")
# def store_status(db: Session = Depends(get_db)):
#     crud.insert_store_status(db)
#     return {"message": "Store status data inserted successfully."}


# # def menu_hour(db: Session = Depends(get_db)):
# #     crud.insert_menu_hours(db)
# #     return 

# @app.post("/insert-bq_results/")
# def bq_results(db: Session = Depends(get_db)):
#     crud.insert_bq_results(db)
#     return {"message": "bq results data inserted successfully."}


# @app.post("/menu_hour/")
# async def menu_hour(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
#     background_tasks.add_task(crud.insert_menu_hours, db)
#     return {"message": "Menu hours insertion request received and enqueued for background execution"}

@app.get("/business_hours/")
def business_hours(db:Session=Depends(get_db)):
    return crud.query(db)

def insert_data(db):
    crud.insert_store_status_update(db)
    crud.insert_store_time_zone(db)
    crud.insert_store_business_hour(db)

@app.post("/trigger_report/")
async def trigger_report(background_tasks: BackgroundTasks, db:Session=Depends(get_db)):
    background_tasks.add_task(insert_data(db))

    return
