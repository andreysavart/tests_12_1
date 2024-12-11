from unittest import TestCase as TC
import unittest

class RunnerTest(TC):
    def test_walk(self):
        first = Runner('Igor')
        for i in range (10):
            first.walk()
        self.assertEqual(first.distance, 50)

    def test_run(self):
        second = Runner('Ben')
        for i in range (10):
            second.run()
        self.assertEqual(second.distance, 100)

    def test_challenge(self):
        walker = Runner('Dasha')
        runner = Runner('Nikita')
        for i in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker,runner)

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


if __name__ == '__main__':
    unittest.main()