
from abc import ABC, abstractmethod

class TractionControll(ABC):

    @abstractmethod
    def volume_up   () : pass

    @abstractmethod
    def volume_down () : pass


class State(ABC):

    @abstractmethod
    def volume_up   () : pass

    @abstractmethod
    def volume_down () : pass



