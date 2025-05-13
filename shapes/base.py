from typing import Self, Type

from mixins.squarable import Squarable


class BaseShape(Squarable):
    registry = {}

    def __init_subclass__(cls) -> None:
        if cls.__name__ in cls.registry:
            raise LookupError(f"class {cls.__name__} already exists!")
        cls.registry[cls.__name__] = cls

    @classmethod
    def get_registered(cls, name: str):
        return cls.registry[name]

    def check_is_valid(self) -> bool:
        return True

    @classmethod
    def build_and_validate(cls: Type[Self], *args, **kwargs) -> Self:
        result = cls(*args, **kwargs)
        if result.check_is_valid():
            return result
        raise ValueError("non valid figure")
