from advent_of_code_2021.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


class Task01(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "There are %d measurements that are larger than their predecessor."
        self.bonus_answer_text = "There are %d sliding window measurements larger than their predecessors."
        self.task_number = 1

    def parse_input(self, input_file_content: List[str]) -> List[int]:
        return [int(line) for line in input_file_content]

    def solve_task(self, input_file_content: List[str]):
        parsed_input = self.parse_input(input_file_content)
        last_measurement = parsed_input[0]
        counter = 0
        for measurement in parsed_input:
            if measurement > last_measurement:
                counter += 1
            last_measurement = measurement
        return counter

    def solve_bonus_task(self, input_file_content: List[str]):
        parsed_input = self.parse_input(input_file_content)
        counter = 0
        last_sum = sum(parsed_input[0:3])
        for i in range(len(parsed_input) - 2):
            current_sum = sum(parsed_input[i:i+3])
            if current_sum > last_sum:
                counter += 1
            last_sum = current_sum
        return counter

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[0-9]+\n?", line) for line in input_file_content)