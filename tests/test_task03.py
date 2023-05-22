from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2021.tasks.task03.task03 import Task03
from advent_of_code_2021.advent_of_code_utils import parse_args


class Task03Tests(TaskTest, unittest.TestCase):
    task = Task03(parse_args([]))
    known_input = ["00100\n",
                   "11110\n",
                   "10110\n",
                   "10111\n",
                   "10101\n",
                   "01111\n",
                   "00111\n",
                   "11100\n",
                   "10000\n",
                   "11001\n",
                   "00010\n",
                   "01010"]
    known_output = 198
    known_bonus_output = -1
