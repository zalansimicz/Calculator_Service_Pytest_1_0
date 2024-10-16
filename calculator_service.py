class CalculatorService:
    def __init__(self, data_repository):
        self._data_repository = data_repository

    def calculate_sum(self, a, b):
        data_from_repo = self._data_repository.get_data()
        return a + b + data_from_repo

    def calculate_multiplication(self, a, b):
        data_from_repo = self._data_repository.get_data()
        return a * b * data_from_repo

    def calculate_division(self, a, b):
        data_from_repo = self._data_repository.get_data()
        return a / b / data_from_repo