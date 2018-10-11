from typing import Optional, NamedTuple


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

