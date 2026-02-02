import pytest

@pytest.fixture
def fake_db():
    db={"users":["admin1","admin2"]}
    yield db
    db.clear()
    
    
def test_db(fake_db):
    assert "admin1" in fake_db["users"]
    