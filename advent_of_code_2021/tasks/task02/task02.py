from advent_of_code_2021.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple
import re


class Task02(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The product of depth and horizontal position is %d."
        self.bonus_answer_text = "The product of depth and the final horizontal position is %d."
        self.task_number = 2

    def parse_input(self, input_file_content) -> List[Tuple[str, int]]:
        return [(line.split()[0], int(line.split()[1])) for line in input_file_content]

    def solve_task(self, input_file_content: List[str]) -> int:
        position = (0, 0)
        for command, value in self.parse_input(input_file_content):
            if command == 'forward':
                position = (position[0] + value, position[1])
            elif command == 'down':
                position = (position[0], position[1] + value)
            elif command == 'up':
                position = (position[0], position[1] - value)
            else:
                raise 'invalid input'
        return position[0] * position[1]

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        position = (0, 0, 0)
        for command, value in self.parse_input(input_file_content):
            if command == 'forward':
                position = (position[0] + value, position[1] + (position[2] * value), position[2])
            elif command == 'down':
                position = (position[0], position[1], position[2] + value)
            elif command == 'up':
                position = (position[0], position[1], position[2] - value)
            else:
                raise 'invalid input'
        return position[0] * position[1]

    def is_input_valid(self, input_file_content: List[str]) -> bool:
        return all(re.fullmatch('(forward|down|up) [0-9]+\n?', line) for line in input_file_content)
