import random

from typing import List, Dict


class ColorGenerator():
    def __init__(self, color_spaces_def: List[Dict]) -> None:
        self.color_spaces_def = color_spaces_def

    def generate(self, color_num: int, mode: str = "random") -> List[Dict]:
        if mode == "random":
            return self.__generate_random(color_num)

        raise Exception("Unexpected mode")

    def __generate_random(self, color_num: int) -> List[Dict]:
        colors: List[Dict] = []

        for _ in range(color_num):
            color_space: Dict = random.choice(self.color_spaces_def)
            components: Dict = {component: random.randint(value_range[0], value_range[1]) for component, value_range in color_space["components"].items()}

            colors.append({
                "type": color_space["name"],
                **components
            })

        return colors

    # Different generator implementations/Algorithms go on below...
