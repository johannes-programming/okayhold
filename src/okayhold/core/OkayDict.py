from typing import *

import setdoc
from datahold import core
from datahold.core.HoldDict import HoldDict
from datahold.core.OkayObject import OkayObject
from frozendict import frozendict

__all__ = ["OkayDict"]


Key = TypeVar("Key")
Value = TypeVar("Value")


class OkayDict(OkayObject, HoldDict[Key, Value]):

    data: frozendict[Key, Value]
    __slots__ = ()

    @setdoc.basic
    def __or__(self: Self, other: Any, /) -> Self:
        return type(self)(self._data | dict(other))
