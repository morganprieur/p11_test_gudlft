
import pytest
from server import app as flask_app 


@pytest.fixture
def app():
    app = flask_app 
    yield app 

@pytest.fixture 
def client(app): 
    return app.test_client() 
