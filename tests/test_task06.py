from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2021.tasks.task06.task06 import Task06
from advent_of_code_2021.advent_of_code_utils import parse_args


class Task06Tests(TaskTest, unittest.TestCase):
    task = Task06(parse_args([]))
    known_input = ["3,4,3,1,2"]
    known_output = 5934
    known_bonus_output = 26984457539
