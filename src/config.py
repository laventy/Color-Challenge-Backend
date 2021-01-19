from typing import Dict, List

COLOR_SPACE_DEF: List[Dict] = [
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
