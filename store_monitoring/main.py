from fastapi import Depends, FastAPI, BackgroundTasks

from .api import report

app = FastAPI()
app.include_router(report.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Store monitoring"}
