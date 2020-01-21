from typing import TypeVar, Generic
import canopy
import json

T = TypeVar('T')


class SerializableValue(Generic[T]):
    def __init__(
            self,
            session: canopy.Session,
            value: T):
        self._session = session
        self.value = value

    def serialize(self) -> str:
        return json.dumps(self._session.async_client.sanitize_for_serialization(self.value))
