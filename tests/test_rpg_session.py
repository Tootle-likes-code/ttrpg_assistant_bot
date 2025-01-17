import unittest
from datetime import datetime

from ttrpg_assistant_bot.rpg_session import RpgSession


class SessionTests(unittest.TestCase):
    def setUp(self):
        self.test_date = datetime(2020, 1, 1)
        self.current_week = 4
        self.weeks_in_run = 14

        self.test_session = RpgSession(self.test_date, self.current_week, self.weeks_in_run)


class InitTests(SessionTests):
    def test_default_weeks_in_run_is_12(self):
        # Arrange
        expected_result = 12
        test_session = RpgSession(datetime(2020, 1, 1), 3)

        # Act
        result = test_session.weeks_in_run

        # Assert
        self.assertEqual(expected_result, result)


class StrTests(SessionTests):   
    def test_str_returns_expected_text(self):
        # Arrange
        expected_result = (f"Next Session is: {self.test_date.strftime("%d/%m/%Y")}.  "
                           f"It is {self.current_week} of {self.weeks_in_run}")

        # Act
        result = str(self.test_session)

        # Assert
        self.assertEqual(expected_result, result)


class EqTests(SessionTests):
    def test_matching_values_returns_true(self):
        # Assert
        self.assertTrue(self.test_session == self.test_session)
        
    def test_not_matching_values_returns_false(self):
        # Arrange
        different_session = RpgSession(self.test_date, 2)

        # Assert
        self.assertFalse(self.test_session == different_session)


if __name__ == '__main__':
    unittest.main()
