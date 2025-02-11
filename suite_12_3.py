import unittest
from tests_12_3 import RunnerTest, TournamentTest


def create_test_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Добавляем тесты используя современный метод
    suite.addTests([
        loader.loadTestsFromTestCase(RunnerTest),
        loader.loadTestsFromTestCase(TournamentTest)
    ])

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = create_test_suite()
    runner.run(suite)