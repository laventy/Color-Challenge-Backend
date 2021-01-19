import pytest

from generator import ColorGenerator
from typing import List, Dict


@pytest.fixture()
def color_spaces():
    return [
        {
            "name": "rgb",
            "components": {
                "red": [0, 255],
                "green": [0, 255],
                "blue": [0, 255]
            }
        },
        {
            "name": "hsl",
            "components": {
                "hue": [0, 360],
                "saturation": [0, 100],
                "lightness": [0, 100]
            }
        }
    ]


class TestGeneratorClass:
    def test_num_of_colors_returned(self, color_spaces):
        colors: List[Dict] = ColorGenerator(color_spaces).generate(color_num=3)

        assert len(colors) == 3

    def test_all_rgb_colors(self, color_spaces, mocker):
        mocker.patch('random.choice', return_value=color_spaces[0])

        colors: List[Dict] = ColorGenerator(color_spaces).generate(color_num=5)

        assert len([color for color in colors if color["type"] == "rgb"]) == 5

    def test_2_rgb_colors_and_2_hsl(self, color_spaces, mocker):
        mocker.patch('random.choice', side_effect=[color_spaces[0], color_spaces[0], color_spaces[1], color_spaces[1]])

        colors: List[Dict] = ColorGenerator(color_spaces).generate(color_num=4)

        assert len([color for color in colors if color["type"] == "rgb"]) == 2
        assert len([color for color in colors if color["type"] == "hsl"]) == 2

    def test_rgb_value_within_rage(self, color_spaces, mocker):
        mocker.patch('random.choice', return_value=color_spaces[0])

        for _ in range(40):
            colors: List[Dict] = ColorGenerator(color_spaces).generate(color_num=1)

            assert 0 <= colors[0]["red"] <= 255
            assert 0 <= colors[0]["green"] <= 255
            assert 0 <= colors[0]["blue"] <= 255
