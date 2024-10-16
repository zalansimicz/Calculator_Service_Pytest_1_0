import pytest
from unittest.mock import Mock
from calculator_service import CalculatorService
from idata_repository import IDataRepository

def test_calculate_sum_with_stub_returns_correct_sum():
    # Arrange: létrehozunk egy mock-ot
    stub_repository = Mock(IDataRepository)
    stub_repository.get_data.return_value = 10

    calculator_service = CalculatorService(stub_repository)
    # Act: meghívjuk a calculate_sum metódust
    result = calculator_service.calculate_sum(5, 3)

    # Assert: ellenőrizzük az eredményt
    assert result == 18     # 5 + 3 + 10 = 18

def test_calculate_sum_with_mock_verifies_get_data_called():
    mock_repository = Mock(IDataRepository)
    mock_repository.get_data.return_value = 10

    calculator_service = CalculatorService(mock_repository)
    result = calculator_service.calculate_sum(5, 3)

    assert result == 18
    # Verify: ellenőrizzük, hogy a get_data metódust egyszer hívták meg
    mock_repository.get_data.assert_called_once()

def test_calculate_multiplication_with_mock_verifies_get_data_called():
    mock_repository = Mock(IDataRepository)
    mock_repository.get_data.return_value = 3

    calculator_service = CalculatorService(mock_repository)
    result = calculator_service.calculate_multiplication(2, 2)
    
    assert result == 12         # 2 * 2 * 3 = 12
    mock_repository.get_data.assert_called_once()

def test_calculate_divison_with_mock_verifies_get_data_called():
    mock_repository = Mock(IDataRepository)
    mock_repository.get_data.return_value = 2

    calculator_service = CalculatorService(mock_repository)
    result = calculator_service.calculate_division(8, 2)
    
    assert result == 2          # 8 / 2 / 2 = 2
    mock_repository.get_data.assert_called_once()