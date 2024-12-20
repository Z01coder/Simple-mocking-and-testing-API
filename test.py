import requests
import pytest
from unittest.mock import patch
from main import get_random_cat_image

@patch('requests.get')
def test_successful_request(mock_get):
    # Мок успешного ответа
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"url": "https://cdn2.thecatapi.com/images/example.jpg"}]

    result = get_random_cat_image()
    assert result == "https://cdn2.thecatapi.com/images/example.jpg"

@patch('requests.get')
def test_unsuccessful_request(mock_get):
    # Мок ответа с ошибкой
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = None

    result = get_random_cat_image()
    assert result is None

@patch('requests.get')
def test_exception_handling(mock_get):
    # Мок выбрасывания исключения
    mock_get.side_effect = requests.RequestException

    result = get_random_cat_image()
    assert result is None

if __name__ == "__main__":
    pytest.main()
