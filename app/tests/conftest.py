import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, get_db
from app.crud.auth import get_current_user
from app.main import app
from fastapi.testclient import TestClient
from app.models import measurement, unit
from app.db.initialization import _init_users

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

    def override_get_current_user():
        return db.Query(User).all()

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = override_get_current_user
    with TestClient(app) as client:
        yield client

@pytest.fixture
def setup_data(db):
    grams = unit.Unit(name="Grams")
    tons = unit.Unit(name="Tons")
    db.add(grams)
    db.add(tons)
    db.commit()
    db.refresh(grams)
    db.refresh(tons)
    db.add(measurement.Measurement(co2_value=100, unit_id=grams.id))
    db.add(measurement.Measurement(co2_value=200, unit_id=grams.id))
    db.add(measurement.Measurement(co2_value=300, unit_id=tons.id))
    _init_users(db)
    db.commit()
    yield
    db.query(measurement.Measurement).delete()
    db.commit()