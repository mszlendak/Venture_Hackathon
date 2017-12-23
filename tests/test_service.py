import platform
import pytest

from venturedevs_python_hahaton import service
from .example_data import EXAMPLE_FORECAST, EXAMPLE_CSV_FILE


@pytest.fixture
def no_woeid_request_fixture(monkeypatch):
    def mock_return(url):
        class ResponseMock():
            status_code = 404
        return ResponseMock()

    monkeypatch.setattr(service.requests, 'get', mock_return)


class TestService:
    def test_get_forecast_from_api_no_woeid(self, no_woeid_request_fixture):
        result = service.get_forecasts_from_api(666)
        assert result is None

    def test_get_forecast_from_api_ok(self, request_fixutre):
        result = service.get_forecasts_from_api(666)
        assert type(result) is dict

    def test_forecast_to_list(self):
        result = service.forecast_to_list(EXAMPLE_FORECAST)
        assert type(result) is list
        assert len(result) == 6
        assert len(result[0]) == 15

    def test_get_forecast_file_path(self):
        result = service.get_forecast_file_path(666)

        assert type(result) is tuple
        assert type(result[0]) is str
        assert type(result[1]) is str

    def test_save_forecast(self, tmpdir):
        tmp_dir = tmpdir.mkdir('forecasts').mkdir('666').mkdir('02-11-2017')
        service.save_forecast(EXAMPLE_FORECAST,
                              tmp_dir,
                              'test.csv')

        files_in_dir = tmp_dir.listdir()
        assert len(files_in_dir) == 1

        tmp_file = files_in_dir[0]

        assert tmp_file.isfile() is True
        assert tmp_file.strpath.endswith(
            'forecasts\\666\\02-11-2017\\test.csv'
            if platform.system() == 'Windows' else
            'forecasts/666/02-11-2017/test.csv'
        ) is True
        assert tmp_file.read() == EXAMPLE_CSV_FILE
