from fastapi import FastAPI, APIRouter
from app.api import measurement, unit, auth
from app.db.database import engine, Base, SessionLocal
from app.db.initialization import data_init

app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc", openapi_url="/api/openapi.json")

api_router = APIRouter()
api_router.include_router(measurement.router, prefix="/measurements", tags=["Measurements"])
api_router.include_router(unit.router, prefix="/units", tags=["Units"])
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])

app.include_router(api_router, prefix="/api")

@app.on_event("startup")
def startup_event():
	db = SessionLocal()
	try:
		data_init(db)
	finally:
		db.close()