from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2021.tasks.task02.task02 import Task02
from advent_of_code_2021.advent_of_code_utils import parse_args


class Task02Tests(TaskTest, unittest.TestCase):
    task = Task02(parse_args([]))
    known_input = ["forward 5\n",
                   "down 5\n",
                   "forward 8\n",
                   "up 3\n",
                   "down 8\n",
                   "forward 2\n"]
    known_output = 150
    known_bonus_output = 900
