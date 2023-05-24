from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2021.tasks.task05.task05 import Task05
from advent_of_code_2021.advent_of_code_utils import parse_args


class Task05Tests(TaskTest, unittest.TestCase):
    task = Task05(parse_args([]))
    known_input = ["0,9 -> 5,9\n",
                   "8,0 -> 0,8\n",
                   "9,4 -> 3,4\n",
                   "2,2 -> 2,1\n",
                   "7,0 -> 7,4\n",
                   "6,4 -> 2,0\n",
                   "0,9 -> 2,9\n",
                   "3,4 -> 1,4\n",
                   "0,0 -> 8,8\n",
                   "5,5 -> 8,2"]
    known_output = 5
    known_bonus_output = 12
