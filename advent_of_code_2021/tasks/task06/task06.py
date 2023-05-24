from advent_of_code_2021.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
from collections import deque

import re


class Task06(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "After 80 days there would be %d lanternfish."
        self.bonus_answer_text = "After 256 days there would be %d lanternfish."
        self.task_number = 6

    def simulate_steps(self, number_of_steps: int, fish_list: List[int]) -> int:
        current_fish = deque()
        for i in range(9):
            current_fish.append(0)
        for fish in fish_list:
            current_fish[fish] += 1
        for i in range(number_of_steps):
            breeders = current_fish.popleft()
            current_fish.append(breeders)
            current_fish[6] += breeders
        return sum(current_fish)

    def solve_task(self, input_file_content: List[str]) -> int:
        return self.simulate_steps(80, [int(x) for x in input_file_content[0].split(',')])

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        return self.simulate_steps(256, [int(x) for x in input_file_content[0].split(',')])

    def is_input_valid(self, input_file_content: List[str]) -> bool:
        return all(re.fullmatch(r'(\d,)*\d\n?', line) for line in input_file_content)
