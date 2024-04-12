import os
import csv
import pytest
from unittest.mock import MagicMock
from scrape_offices import scrape_offices

@pytest.fixture
def mock_webdriver():
    return MagicMock()

@pytest.fixture
def mock_csv_writer():
    return MagicMock()

# Проверка основного функционала scrape_offices
def test_scrape_offices(mock_webdriver, mock_csv_writer):
    output_file_path = "test_contacts.csv"
    scrape_offices(output_file_path, mock_webdriver, mock_csv_writer)
    assert mock_webdriver.get.called
    assert mock_webdriver.find_element.call_count == 2
    assert mock_webdriver.find_elements.called
    assert mock_csv_writer.writerow.call_count == 5
    print("Тест test_scrape_offices успешно завершен.")

# Проверка обработки 
def test_scrape_offices_invalid_output_path(mock_webdriver, mock_csv_writer):
    output_file_path = "C:\\Users\\Wolne\\OneDrive\\Desktop\\тест2\\scrape_offices.py\\contacts"  
    with pytest.raises(Exception):
        scrape_offices(output_file_path, mock_webdriver, mock_csv_writer)
    print("Тест test_scrape_offices_invalid_output_path успешно завершен.")

# Проверка  при невозможности найти элементы
def test_scrape_offices_invalid_web_elements(mock_webdriver, mock_csv_writer):
    output_file_path = "test_contacts.csv"
    mock_webdriver.find_elements.return_value = []  
    with pytest.raises(Exception):
        scrape_offices(output_file_path, mock_webdriver, mock_csv_writer)
    print("Тест test_scrape_offices_invalid_web_elements успешно завершен.")

# Проверка некорректной записи в CSV файл
def test_scrape_offices_invalid_csv_write(mock_webdriver, mock_csv_writer):
    output_file_path = "contacts.csv"
    mock_csv_writer.writerow.side_effect = Exception()  
    with pytest.raises(Exception):
        scrape_offices(output_file_path, mock_webdriver, mock_csv_writer)
    print("Тест test_scrape_offices_invalid_csv_write успешно завершен.")


