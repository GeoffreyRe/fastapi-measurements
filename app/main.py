from fastapi import FastAPI
from app.api import measurement, unit
from app.db.database import engine, Base, SessionLocal
from app.db.initialization import data_init

app = FastAPI()

app.include_router(measurement.router, prefix="/measurements", tags=["Measurements"])
app.include_router(unit.router, prefix="/units", tags=["Units"])

@app.on_event("startup")
def startup_event():
	db = SessionLocal()
	try:
		data_init(db)
	finally:
		db.close()