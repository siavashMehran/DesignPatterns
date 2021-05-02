from typing import Any
from observerConcrete import ObserverConcrete
from interface import _ObservableInterface, _ObserverInteface

class ObservableConcrete(_ObservableInterface):
    
    
    
    def __init__(self):
        self._data = Any
        self._clients = set()


    def _notify(self):
        """
        to notify every client in __client
        this gets called when (Observable) changes state
        for every client, it calls => update()
        """
        for client in (self._clients):
            client.update()


    def _add(self, client:ObserverConcrete):
        """
        for adding clients to __client
        it shoud recieve an instance of ( Observer ) class
        this will not be called directly 
        when we create an instance add() should be called automatically
        """
        self._clients.add(client)
    

    def remove(self, client):
        """
        for removing clients from __client
        it shoud recieve an instance of ( Observer ) class
        """
        if client in (self._clients):
            self._clients.remove(client)
        else: print('not a client')


    def get_data(self):
        """
        returns tha data of the Observable
        """
        return self._data

    def set_data(self, data:Any):
        """
        set the data to a new value and automatically notify all the CLIENTS
        data can be ANY and this function doesnt return anything
        additional logic for updating the Observable shoud be here
        """
        self._data = data
        self._notify()

    def get_clients(self):
        """
        returns the registered CLIENTS as a list
        clients are originally stored as a set()
        """
        return [x for x in self._clients]







class ObserverConcrete(_ObserverInteface):

    def __init__(self, observable):
        self._data = Any
        self.observable = observable
        self.observable._add(self)

    def update(self):
        self._data = self.observable.get_data()

    def get_data(self):
        return self._data


