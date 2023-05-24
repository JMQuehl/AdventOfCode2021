import copy

from advent_of_code_2021.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple
import re


class Task05(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "Two or more lines overlap at %d points."
        self.bonus_answer_text = "Two or more lines overlap at %d points."
        self.task_number = 5

    def parse_input(self, input_file_content: List[str]) -> List[List[int]]:
        coordinates = []
        for line in input_file_content:
            coordinates.append([int(x) for x in re.findall(r'\d+', line)])
        return coordinates

    def add_line(self, line_coordinates: List[int], board: List[List[int]]):
        x_direction = 0 if (line_coordinates[2] - line_coordinates[0]) == 0 \
            else int((line_coordinates[2] - line_coordinates[0])/abs(line_coordinates[2] - line_coordinates[0]))
        y_direction = 0 if (line_coordinates[3] - line_coordinates[1]) == 0 \
            else int((line_coordinates[3] - line_coordinates[1])/abs(line_coordinates[3] - line_coordinates[1]))
        current_coordinate = (line_coordinates[0], line_coordinates[1])
        goal_coordinate = (line_coordinates[2], line_coordinates[3])
        while current_coordinate != goal_coordinate:
            board[current_coordinate[0]][current_coordinate[1]] += 1
            current_coordinate = (current_coordinate[0] + x_direction, current_coordinate[1] + y_direction)
        board[current_coordinate[0]][current_coordinate[1]] += 1

    def solve_task(self, input_file_content: List[str]) -> int:
        line_coordinates = self.parse_input(input_file_content)
        max_coordinate = max([max(x) for x in line_coordinates]) + 1
        board = [[0 for x in range(max_coordinate)] for y in range(max_coordinate)]
        for coordinates in line_coordinates:
            if coordinates[0] == coordinates[2] or coordinates[1] == coordinates[3]:
                self.add_line(coordinates, board)
        return sum([sum(x > 1 for x in y) for y in board])

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        line_coordinates = self.parse_input(input_file_content)
        max_coordinate = max([max(x) for x in line_coordinates]) + 1
        board = [[0 for x in range(max_coordinate)] for y in range(max_coordinate)]
        for coordinates in line_coordinates:
                self.add_line(coordinates, board)
        return sum([sum(x > 1 for x in y) for y in board])

    def is_input_valid(self, input_file_content: List[str]) -> bool:
        return all(re.fullmatch('[0-9]+,[0-9]+ -> [0-9]+,[0-9]+\n?', line) for line in input_file_content)
