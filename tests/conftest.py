import pytest

from venturedevs_python_hahaton.app import APP
from venturedevs_python_hahaton import service

from example_data import EXAMPLE_FORECAST


@pytest.fixture
def app():
    APP.debug = True
    return APP


@pytest.fixture
def request_fixutre(monkeypatch):
    def mock_return(url):
        class ResponseMock():
            status_code = 200

            def json(self):
                return EXAMPLE_FORECAST
        return ResponseMock()

    monkeypatch.setattr(service.requests, 'get', mock_return)
