import unittest
import logging
from rt_with_exceptions import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s - %(message)s'
)

def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.__class__.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Тесты активны

    @skip_if_frozen
    def test_walk(self):
        """Тест метода walk с обработкой исключений скорости"""
        try:
            # Намеренно передаем отрицательную скорость
            runner = Runner("Test Walker", speed=-5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", str(e))

    @skip_if_frozen
    def test_run(self):
        """Тест метода run с обработкой исключений имени"""
        try:
            # Намеренно передаем неверный тип имени
            runner = Runner(12345, speed=10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", str(e))

    @skip_if_frozen
    def test_challenge(self):
        """Тест сравнения бегунов без изменений"""
        runner1 = Runner("Challenger 1", 5)
        runner2 = Runner("Challenger 2", 5)
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main(verbosity=2)