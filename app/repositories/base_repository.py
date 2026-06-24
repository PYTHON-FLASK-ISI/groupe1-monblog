from typing import TypeVar, Generic

T = TypeVar('T')

class BaseRepository(Generic[T]):

    def __init__(self):
        self._items : dict[int, T] = {}
        self._next_id = 1

    def enregistrer(self, obj: T) -> T:
        if getattr(obj, 'id', None) is None:
            obj.id = self._next_id
            self._next_id += 1
        self._items[obj.id] = obj
        return obj

    def get(self, id: int) -> T:
        return self._items.get(id)

    def lister(self) -> list[T]:
        return list(self._items.values())

    def supprimer(self, id: int) -> bool:
        return self._items.pop(id, None) is not None
