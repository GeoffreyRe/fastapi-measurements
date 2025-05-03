from app.models.measurement import Measurement
from app.models.unit import Unit

# GET tests
def test_get_measurements(client, setup_data):
    response = client.get("/measurements")
    
    assert response.status_code == 200

    measurements = response.json()
    assert len(measurements) == 2

# CREATE tests
def test_create_measurement(client, db, setup_data):
    unit_id = db.query(Unit).filter(Unit.name == 'Grams').first()
    data = {"co2_value": 150, "unit_id": unit_id.id}
    response = client.post("/measurements", json=data)
    
    assert response.status_code == 201
    measurement = response.json()
    
    db_measurement = db.query(Measurement).filter_by(id=measurement["id"]).first()
    assert db_measurement is not None
    assert db_measurement.co2_value == 150

def test_create_measurement_string_value(client, db, setup_data):
    unit_id = db.query(Unit).filter(Unit.name == 'Grams').first()
    data = {"co2_value": "test", "unit_id": unit_id.id}
    response = client.post("/measurements", json=data)
    
    assert response.status_code == 422