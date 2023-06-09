from advent_of_code_2021.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


class TaskXX(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = '%d.'
        self.bonus_answer_text = '%d.'
        self.task_number = 0

    def parse_input(self, input_file_content: List[str]):
        return 0

    def solve_task(self, input_file_content: List[str]):
        return 0

    def solve_bonus_task(self, input_file_content: List[str]):
        return 0

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("", line) for line in input_file_content)
