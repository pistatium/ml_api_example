from typing import Optional, NamedTuple

import numpy as np


class Item(NamedTuple):
    x1: int
    x2: int
    x3: int
    x4: int
    x5: int
    y: Optional[int] = None

    @classmethod
    def from_dict(cls, d: dict):
        return Item(**d)

    def to_vec(self):
        return np.array([self.x1, self.x2, self.x3, self.x4, self.x5]), np.array([self.y])
