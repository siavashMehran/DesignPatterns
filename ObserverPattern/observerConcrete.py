
from typing import Any
from interface import _ObserverInteface


class ObserverConcrete(_ObserverInteface):

    def __init__(self, observable):
        self._data = Any
        self.observable = observable
        self.observable._add(self)

    def update(self):
        self._data = self.observable.get_data()

    def get_data(self):
        return self._data


