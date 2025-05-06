from app.models.measurement import Measurement
from app.models.unit import Unit
from sqlalchemy import func

# GET tests
def test_get_measurements(db, client, setup_data):
    db_measurements = db.query(Measurement).all()
    response = client.get("/measurements")
    
    assert response.status_code == 200

    measurements = response.json()
    assert len(measurements) == len(db_measurements)

def test_get_measurements_with_limit(client, setup_data):
    response = client.get("/measurements", params={'limit': 1})
    
    assert response.status_code == 200

    measurements = response.json()
    assert len(measurements) == 1

def test_get_measurements_with_unit(db, client, setup_data):
    unit_id = db.query(Unit).filter(Unit.name == 'Tons').first()
    db_measurements = db.query(Measurement).filter(Measurement.unit_id == unit_id.id).all()
    response = client.get("/measurements", params={'unit_id': unit_id.id})
    
    assert response.status_code == 200

    measurements = response.json()
    assert len(measurements) == len(db_measurements)

def test_get_measurements_with_invalid_unit(db, client, setup_data):
    unit_id = db.query(func.max(Unit.id)).scalar() + 1
    response = client.get("/measurements", params={'unit_id': unit_id})
    
    assert response.status_code == 404

def test_get_measurement(db, client, setup_data):
    measurement = db.query(Measurement).first()
    response = client.get(f"/measurements/{measurement.id}")
    
    assert response.status_code == 200

    measurement_response = response.json()

    assert measurement_response['id'] == measurement.id
    assert measurement_response['co2_value'] == measurement.co2_value

def test_get_measurement_unknown_id(db, client, setup_data):
    measurement_id = db.query(func.max(Measurement.id)).scalar() + 1
    response = client.get(f"/measurements/{measurement_id}")
    
    assert response.status_code == 404

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

def test_create_measurement_string_co2_value(client, db, setup_data):
    unit_id = db.query(Unit).filter(Unit.name == 'Grams').first()
    data = {"co2_value": "test", "unit_id": unit_id.id}
    response = client.post("/measurements", json=data)
    
    assert response.status_code == 422

def test_create_measurement_without_unit(client, db, setup_data):
    data = {"co2_value": 150}
    response = client.post("/measurements", json=data)
    
    assert response.status_code == 422

def test_create_measurement_unknown_unit(client, db, setup_data):
    # unknown id
    unit_id = db.query(func.max(Unit.id)).scalar() + 1
    data = {"co2_value": 150, 'unit_id': unit_id}
    response = client.post("/measurements", json=data)
    
    assert response.status_code == 404

# UPDATE TESTS
def test_update_measurement(client, db, setup_data):
    unit_id = db.query(Unit).filter(Unit.name == 'Tons').first()
    measurement_id = db.query(Measurement).first()

    assert measurement_id.co2_value != 250
    assert measurement_id.unit_id != unit_id.id
    data = {"co2_value": 250, "unit_id": unit_id.id}
    response = client.patch(f"/measurements/{measurement_id.id}", json=data)
    
    assert response.status_code == 200
    measurement = response.json()
    
    assert measurement_id.co2_value == 250
    assert measurement_id.unit_id == unit_id.id

def test_update_measurement_null_unit(client, db, setup_data):
    measurement_id = db.query(Measurement).first()

    data = {"co2_value": 250, "unit_id": None}
    response = client.patch(f"/measurements/{measurement_id.id}", json=data)

    assert response.status_code == 422

def test_update_measurement_string_co2_value(client, db, setup_data):
    measurement_id = db.query(Measurement).first()
    data = {"co2_value": "test"}
    response = client.patch(f"/measurements/{measurement_id.id}", json=data)
    
    assert response.status_code == 422

def test_update_measurement_unknown_id(client, db, setup_data):
    measurement_id = db.query(func.max(Measurement.id)).scalar() + 1

    data = {"co2_value": 250}
    response = client.patch(f"/measurements/{measurement_id}", json=data)
    
    assert response.status_code == 404

# DELETE TESTS
def test_delete_measurement(client, db, setup_data):
    inital_measurement_ids = db.query(Measurement).all()
    measurement_to_delete = inital_measurement_ids[0].id

    response = client.delete(f"/measurements/{measurement_to_delete}")
    
    after_measurement_ids = db.query(Measurement).all()
    deleted_measurement_id = db.query(Measurement).filter_by(id=measurement_to_delete).first()

    assert response.status_code == 204
    assert len(after_measurement_ids) == len(inital_measurement_ids) - 1
    assert deleted_measurement_id is None

def test_delete_measurement_unknown_id(client, db, setup_data):
    inital_measurement_ids = db.query(Measurement).all()
    measurement_id = db.query(func.max(Measurement.id)).scalar() + 1


    response = client.delete(f"/measurements/{measurement_id}")
    
    after_measurement_ids = db.query(Measurement).all()

    assert response.status_code == 404
    assert len(after_measurement_ids) == len(inital_measurement_ids)

