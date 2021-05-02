#this file should only contain interfaces rather than concrete classes
from abc import ABC, abstractmethod
from typing import Any
class _ObservableInterface(ABC):

    # for adding clients to __client
    # it shoud recieve an instance of ( Observer ) class
    # this will not be called directly 
    # when we create an instance add() should be called automatically
    @abstractmethod
    def _add(client) : pass

    # to notify every client in __client
    # this gets called when (Observable) changes state
    # for every client, it calls => update()
    @abstractmethod
    def _notify() : pass

    # for removing clients from __client
    # it shoud recieve an instance of ( Observer ) class
    @abstractmethod
    def remove(client) : pass

class _ObserverInteface(ABC):

    @abstractmethod
    def update(): pass




