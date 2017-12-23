import pytest

from venturedevs_python_hahaton import app


@pytest.fixture()
def raise_request_error(monkeypatch):
    def mock_return():
        raise Exception('Error')

    monkeypatch.setattr(app, 'get_forecasts_from_api', mock_return)


class TestApp:
    def test_update_forecast_ok(self, client, request_fixutre):
        response = client.post('/update-forecast/523920')
        assert response.status_code == 201
        assert response.json == {'updated': 'ok'}

    def test_update_forecast_not_found(self, client):
        response = client.post('/update-forecast/523920123123234666')
        assert response.status_code == 404

    def test_update_forecast_only_post_allowed(self, client, request_fixutre):
        response = client.post('/update-forecast/523920')
        assert response.status_code == 201

        response = client.get('/update-forecast/523920')
        assert response.status_code == 405

        response = client.delete('/update-forecast/523920')
        assert response.status_code == 405

        response = client.put('/update-forecast/523920')
        assert response.status_code == 405

        response = client.patch('/update-forecast/523920')
        assert response.status_code == 405

    def test_update_forecast_request_error(self, client, raise_request_error):
        response = client.post('/update-forecast/523920')
        assert response.status_code == 502

    def test_update_forecast_bad_param(self, client):
        response = client.post('/update-forecast/ala-ma-kota')
        assert response.status_code == 404
