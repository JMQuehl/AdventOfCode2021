from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2021.tasks.task01.task01 import Task01
from advent_of_code_2021.advent_of_code_utils import parse_args


class Task01Tests(TaskTest, unittest.TestCase):
    task = Task01(parse_args([]))
    known_input = ["199\n",
                   "200\n",
                   "208\n",
                   "210\n",
                   "200\n",
                   "207\n",
                   "240\n",
                   "269\n",
                   "260\n",
                   "263\n"]
    known_output = 7
    known_bonus_output = 5
