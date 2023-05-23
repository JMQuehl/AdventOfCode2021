import copy

from advent_of_code_2021.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Dict
import re


class CountingPrefixNode:
    number_of_words: int
    children: Dict[str, 'CountingPrefixNode']

    def __init__(self, input_string: str):
        self.number_of_words = 0
        self.children = {}
        if len(input_string) >= 1:
            self.add_suffix(input_string)

    def add_suffix(self, suffix_string: str):
        if suffix_string[0] in self.children and len(suffix_string) > 1:
            self.children[suffix_string[0]].add_suffix(suffix_string[1:])
        else:
            self.children[suffix_string[0]] = CountingPrefixNode(suffix_string[1:])
        self.number_of_words += 1


class Task03(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The power consumption of the submarine is %d."
        self.bonus_answer_text = "The life support rating of the submarine is %d."
        self.task_number = 3

    def calculate_gamma_and_epsilon(self, input_strings: List[str]) -> (str, str):
        bit_counter = [0] * len(input_strings)
        for number in input_strings:
            bit_counter = list(map(sum, zip(bit_counter, [int(x) for x in number.rstrip()])))
        gamma_string = "".join(str(round(x / len(input_strings))) for x in bit_counter)
        epsilon_string = "".join(str(1 - round(x / len(input_strings))) for x in bit_counter)
        return int(gamma_string, 2), int(epsilon_string, 2)

    def solve_task(self, input_file_content: List[str]) -> int:
        gamma, epsilon = self.calculate_gamma_and_epsilon([x.rstrip() for x in input_file_content])
        return gamma * epsilon

    def solve_bonus_task(self, input_file_content: List[str]) -> int:
        root_node = CountingPrefixNode('')
        for input_string in [x.rstrip() for x in input_file_content]:
            root_node.add_suffix(input_string)
        current_node = root_node
        current_oxygen_string = ""
        while len(current_node.children) > 0:
            max_value = 0
            max_character = ''
            next_node = None
            for character, remaining_tree in current_node.children.items():
                if remaining_tree.number_of_words > max_value:
                    next_node = remaining_tree
                    max_value = remaining_tree.number_of_words
                    max_character = character
                elif remaining_tree.number_of_words == max_value and character == '1':
                    next_node = remaining_tree
                    max_character = character
            current_oxygen_string += max_character
            current_node = next_node
        current_co2_string = ''
        current_node = root_node
        while len(current_node.children) > 0:
            min_value = float('inf')
            min_character = ''
            next_node = None
            for character, remaining_tree in current_node.children.items():
                if remaining_tree.number_of_words < min_value:
                    next_node = remaining_tree
                    min_value = remaining_tree.number_of_words
                    min_character = character
                elif remaining_tree.number_of_words == min_value and character == '0':
                    next_node = remaining_tree
                    min_character = character
            current_co2_string += min_character
            current_node = next_node
        return int(current_co2_string, 2) * int(current_oxygen_string, 2)

    def is_input_valid(self, input_file_content: List[str]) -> bool:
        return all(re.fullmatch("[01]+\n?", line) for line in input_file_content)
