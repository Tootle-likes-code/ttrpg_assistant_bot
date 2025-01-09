import json
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from requests import HTTPError

from ttrpg_assistant_bot.bank_holidays import bank_holiday_api

TEST_FILE_LOCATION = Path("test_files/extract_example.json")


class RetrieveHolidaysRootTests(unittest.TestCase):
    test_data = None

    @classmethod
    def setUpClass(cls):
        with open(TEST_FILE_LOCATION, "r") as file:
            cls.test_data = json.load(file)


@patch("requests.get")
class RetrieveHolidaysRequestsTests(RetrieveHolidaysRootTests):
    def test_get_called_once(self, mock_request):
        # Arrange
        mock_request.return_value.status_code = 200

        # Act
        bank_holiday_api.retrieve_holidays()

        # Assert
        mock_request.assert_called_once()

    def test_get_goes_to_correct_endpoint(self, mock_request):
        # Arrange
        expected_result = 'https://www.gov.uk/bank-holidays.json'
        mock_request.return_value.status_code = 200

        # Act
        bank_holiday_api.retrieve_holidays()

        # Assert
        mock_request.assert_called_with(expected_result)

    def test_get_returns_non_200_status_code_raise_http_error(self, mock_request):
        # Arrange
        mock_request.return_value.status_code = 404

        # Assert
        with self.assertRaises(HTTPError):
            # Act
            bank_holiday_api.retrieve_holidays()

    def test_get_returns_non_200_status_code_returns_correct_message(self, mock_request):
        # Arrange
        mock_request.return_value.status_code = 404
        mock_request.return_value.text = "Expected to fail"
        expected_message = "Expected to fail"

        # Assert
        with self.assertRaises(HTTPError) as ex:
            # Act
            bank_holiday_api.retrieve_holidays()

        # Assert
        message = str(ex.exception)
        self.assertEqual(expected_message, message)

    def test_returned_value_returns_expected_list_of_date_times(self, mock_request):
        # Arrange
        expected_result = [
            datetime(2019, 1, 1),
            datetime(2019, 4, 19),
            datetime(2019, 4, 22),
            datetime(2019, 5, 6),
            datetime(2019, 5, 27),
            datetime(2019, 8, 26),
            datetime(2019, 12, 25),
            datetime(2019, 12, 26),
            datetime(2020, 1, 1),
            datetime(2020, 4, 10),
            datetime(2020, 4, 13),
            datetime(2020, 5, 8),
            datetime(2020, 5, 25),
            datetime(2020, 8, 31),
            datetime(2020, 12, 25),
            datetime(2020, 12, 28),
            datetime(2021, 1, 1),
            datetime(2021, 4, 2),
            datetime(2021, 4, 5),
            datetime(2021, 5, 3),
            datetime(2021, 5, 31),
            datetime(2021, 8, 30),
            datetime(2021, 12, 27),
            datetime(2021, 12, 28),
            datetime(2022, 1, 3),
            datetime(2022, 4, 15),
            datetime(2022, 4, 18),
            datetime(2022, 5, 2),
            datetime(2022, 6, 2),
            datetime(2022, 6, 3),
            datetime(2022, 8, 29),
            datetime(2022, 9, 19),
            datetime(2022, 12, 26),
            datetime(2022, 12, 27),
            datetime(2023, 1, 2),
            datetime(2023, 4, 7),
            datetime(2023, 4, 10),
            datetime(2023, 5, 1),
            datetime(2023, 5, 8),
            datetime(2023, 5, 29),
            datetime(2023, 8, 28),
            datetime(2023, 12, 25),
            datetime(2023, 12, 26),
            datetime(2024, 1, 1),
            datetime(2024, 3, 29),
            datetime(2024, 4, 1),
            datetime(2024, 5, 6),
            datetime(2024, 5, 27),
            datetime(2024, 8, 26),
            datetime(2024, 12, 25),
            datetime(2024, 12, 26),
            datetime(2025, 1, 1),
            datetime(2025, 4, 18),
            datetime(2025, 4, 21),
            datetime(2025, 5, 5),
            datetime(2025, 5, 26),
            datetime(2025, 8, 25),
            datetime(2025, 12, 25),
            datetime(2025, 12, 26),
            datetime(2026, 1, 1),
            datetime(2026, 4, 3),
            datetime(2026, 4, 6),
            datetime(2026, 5, 4),
            datetime(2026, 5, 25),
            datetime(2026, 8, 31),
            datetime(2026, 12, 25),
            datetime(2026, 12, 28),
            datetime(2027, 1, 1),
            datetime(2027, 3, 26),
            datetime(2027, 3, 29),
            datetime(2027, 5, 3),
            datetime(2027, 5, 31),
            datetime(2027, 8, 30),
            datetime(2027, 12, 27),
            datetime(2027, 12, 28)
        ]
        mock_request.return_value.json.return_value = self.test_data
        mock_request.return_value.status_code = 200

        # Act
        result = bank_holiday_api.retrieve_holidays()

        # Assert
        self.assertEqual(expected_result, result)

