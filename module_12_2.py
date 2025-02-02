import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    """
    Проблема заключается в том что на определенных дистанциях спортсмены за один шаг прибегут к финишу одновременно  
    и в результате получится что тот спортсмен имя которого стоит первым в списке, на таких дистанциях
    окажется первым несмотря на то что может бежать медленнее.
    решение проблемы может быть различным , к примеру , добавление в итоговый 
    список финишеров, после дополнительной сортировки полученного списка финишировавших бегунов на определенном шаге 
    по общей дистанции в забеге. 
    """
    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("\nРезультаты всех тестов:")
        for key, value in cls.all_results.items():
            print(f"{key}: { {k: str(v) for k, v in value.items()} }")

    def test_race1(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results[1] = result

    def test_race2(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = result

    def test_race3(self):
        tournament = Tournament(1, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[3] = result

    # Дополнительный тест для проверки ошибки турнира на короткой дистанции:(distance = 1)
    # на длинных дистанциях (distance > 2) тест пройдет без ошибок
    def test_speed_order(self):
        fast_runner = Runner("Быстрый", 20)
        slow_runner = Runner("Медленный", 1)
        tournament = Tournament(1, slow_runner, fast_runner)
        result = tournament.start()
        self.assertEqual(result[1], fast_runner)
        self.assertEqual(result[2], slow_runner)


if __name__ == "__main__":
    unittest.main(verbosity=2)