import unittest
from runner_and_tournament import Runner, Tournament

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
        runner = Runner("Test Walker", 5)
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Test Runner", 5)
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Challenger 1", 5)
        runner2 = Runner("Challenger 2", 5)
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Тесты заморожены

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        pass  # Вывод результатов перенесен в тесты

    @skip_if_frozen
    def test_race1(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results[1] = {k: str(v) for k, v in result.items()}
        self.assertEqual(list(result.values())[-1].name, "Ник")

    @skip_if_frozen
    def test_race2(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = {k: str(v) for k, v in result.items()}
        self.assertEqual(list(result.values())[-1].name, "Ник")

    @skip_if_frozen
    def test_race3(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[3] = {k: str(v) for k, v in result.items()}
        self.assertEqual(list(result.values())[-1].name, "Ник")