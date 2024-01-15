from abc import ABC
from typing import Any


class SouceMessager(ABC):

    async def read(self, source) -> Any:
        pass
