from advent_of_code_2021.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


class Task03(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The power consumption of the submarine is %d."
        self.bonus_answer_text = "%d."
        self.task_number = 3

    def solve_task(self, input_file_content: List[str]) -> int:
        bit_counter = [0] * len(input_file_content[0].rstrip())
        for number in input_file_content:
            bit_counter = list(map(sum, zip(bit_counter, [int(x) for x in number.rstrip()])))
        gamma_string = "".join(str(round(x/len(input_file_content))) for x in bit_counter)
        gamma = int(gamma_string, 2)
        epsilon_string = "".join(str(1-round(x / len(input_file_content))) for x in bit_counter)
        epsilon = int(epsilon_string, 2)
        return gamma * epsilon

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        return -1

    def is_input_valid(self, input_file_content: List[str]) -> bool:
        return all(re.fullmatch("[01]+\n?", line) for line in input_file_content)
