import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, get_db
from app.main import app
from fastapi.testclient import TestClient
from app.models import measurement, unit

SQLALCHEMY_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client

@pytest.fixture
def setup_data(db):
    db.add(unit.Unit(name="Grams"))
    db.add(unit.Unit(name="Tons"))
    db.commit()
    db.add(measurement.Measurement(co2_value=100, unit_id=1))
    db.add(measurement.Measurement(co2_value=200, unit_id=1))
    db.commit()
    yield
    db.query(measurement.Measurement).delete()
    db.commit()