from app.models.unit import Unit
from sqlalchemy import func

# GET tests
def test_get_units(client, setup_data, auth_token_header):
    headers = {}
    headers.update(auth_token_header)
    response = client.get("/units", headers=headers)
    
    assert response.status_code == 200

    measurements = response.json()
    assert len(measurements) == 2

def test_get_unit(db, client, setup_data, auth_token_header):
    headers = {}
    headers.update(auth_token_header)
    unit = db.query(Unit).first()
    response = client.get(f"/units/{unit.id}", headers=headers)
    
    assert response.status_code == 200

    unit_response = response.json()

    assert unit_response['id'] == unit.id
    assert unit_response['name'] == unit.name

def test_get_unit_unknown_id(db, client, setup_data, auth_token_header):
    headers = {}
    headers.update(auth_token_header)
    unit_id = db.query(func.max(Unit.id)).scalar() + 1
    response = client.get(f"/units/{unit_id}", headers=headers)
    
    assert response.status_code == 404