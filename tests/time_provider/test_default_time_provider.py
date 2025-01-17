import unittest
from datetime import datetime

from ttrpg_assistant_bot.time_provider.default_time_provider import DefaultTimeProvider


class DefaultTimeProviderTests(unittest.TestCase):
    pass


class GetInstanceTests(DefaultTimeProviderTests):
    def setUp(self):
        super().setUp()
        DefaultTimeProvider.instance = None

    def test_instance_starts_as_none(self):
        # Assert
        self.assertIsNone(DefaultTimeProvider.instance)


    def test_no_instance_creates_instance(self):
        # Assert
        self.assertIsNotNone(DefaultTimeProvider.get_instance())

    def test_get_instance_retrieves_existing_instance(self):
        # Arrange
        existing_instance = DefaultTimeProvider()
        expected_result = existing_instance
        DefaultTimeProvider.instance = existing_instance

        # Act
        result = DefaultTimeProvider.get_instance()

        # Assert
        self.assertEqual(expected_result, result)


class GetTimeTests(DefaultTimeProviderTests):
    def convert_time(self, date_time: datetime) -> str:
        return date_time.strftime("%Y-%m-%d %H:%M:%S")

    def assertDatesEqual(self, expected_date, test_date):
        self.assertEqual(self.convert_time(expected_date), self.convert_time(test_date))

    def test_returns_date_time_now_value(self):
        # Arrange
        expected_result = datetime.now()

        # Act
        result = DefaultTimeProvider.get_instance().get_time()

        # Assert
        self.assertDatesEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
