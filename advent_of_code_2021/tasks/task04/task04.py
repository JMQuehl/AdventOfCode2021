import copy

from advent_of_code_2021.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Dict
import re


class Board:

    def __init__(self, string_list: List[str]):
        self.numbers = [[] for x in range(5)]
        self.marked = [[False for y in range(5)] for x in range(5)]

        for i, line in enumerate(string_list):
            self.numbers[i] = [int(x) for x in line.rstrip().split()]
            # first coordinate points downwards in the visualization

    def check_if_won(self) -> bool:
        for i in range(len(self.marked)):
            if all(self.marked[i]):
                return True
        for j in range(len(self.marked[0])):
            if all([self.marked[i][j] for i in range(len(self.marked))]):
                return True

    def mark_number(self, number: int) -> bool:
        found = False
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if self.numbers[i][j] == number:
                    self.marked[i][j] = True
                    found = True
                    break
            if found:
                break
        return found and self.check_if_won()

    def get_sum_of_unmarked(self) -> int:
        sum_of_unmarked = 0
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[i])):
                if not self.marked[i][j]:
                    sum_of_unmarked += self.numbers[i][j]
        return sum_of_unmarked


class Task04(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "My final score if I choose the board that will win first will be %d."
        self.bonus_answer_text = "The final score if I choose the board that will win last will be %d."
        self.task_number = 4

    def parse_input(self, input_file_content: List[str]) -> (List[int], List[Board]):
        assert (self.is_input_valid(input_file_content))

        input_sequence = [int(x) for x in input_file_content[0].rstrip().split(',')]
        boards = []
        for i in range((len(input_file_content) - 1) // 6):
            boards.append(Board(input_file_content[(i * 6) + 2: (i * 6) + 7]))
        return input_sequence, boards

    def solve_task(self, input_file_content: List[str]) -> int:
        input_sequence, boards = self.parse_input(input_file_content)
        for number in input_sequence:
            for board in boards:
                if board.mark_number(number):
                    return board.get_sum_of_unmarked() * number
        return -1

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        input_sequence, boards = self.parse_input(input_file_content)
        remaining_boards = boards
        for number in input_sequence:
            if len(remaining_boards) > 1:
                remaining_boards = [board for board in remaining_boards if not board.mark_number(number)]
            elif remaining_boards[0].mark_number(number):
                return remaining_boards[0].get_sum_of_unmarked() * number
        return -1

    def is_input_valid(self, input_file_content: List[str]) -> bool:
        valid = len(input_file_content) > 6 and re.fullmatch('([0-9]+,)*[0-9]+\n?', input_file_content[0])
        valid = valid and re.fullmatch('\n?', input_file_content[1])
        for i in range(2, len(input_file_content)):
            if not i % 6 == 1:
                valid = valid and re.fullmatch('( *[0-9]+ +){4}[0-9]+\n?', input_file_content[i])
            else:
                valid = valid and re.fullmatch('\n?', input_file_content[i])
            if not valid:
                break
        return valid
