from typing import Any
from src.interface import _ObservableInterface, _ObserverInteface

def ss(s):
    print(s)

# these classes shoud be replaced with the allowed operations
class Operation:
    allowd_operations = ['Update', 'Delete', 'Create']
class Create(Operation):
    pass
class Update(Operation):
    pass
class Delete(Operation):
    pass


# this class exists due to single responsibillity principle
# for our notifier to keep its single responsibility,
#  it can not save the last state of the database
class DatabaseStateRecorder:

    def __init__(self):
        self.last_state:str = Any

    def set_last_state(self, last_state):
        self.last_state = last_state

    def get_last_state(self):
        return self.last_state



class DatabaseNotifier(_ObservableInterface):
    
    def __init__(self, stateRecorder:DatabaseStateRecorder):
        self._clients = set()
        self._allowed_operations = Operation.allowd_operations
        self._stateRecorder = stateRecorder


    # im not sure if the observers should get the data from (DatabaseNotifier)
    # or (DatabaseStateRecorder) 
    # i think its better not to pass the last state to clients directly
    def _notify(self):
        for client in self._clients:
            client.update()      

    def _add(self, client):
        self._clients.add(client)

    def remove(self, client):

        if client in self._clients:
            self._clients.remove(client)
        else : print('not a subscriber')

    def get_last_state(self) -> str():
        return self._stateRecorder.get_last_state()

    def operation(self, operation_type:str, notify:bool=True):

        if (operation_type in self._allowed_operations) and notify:

            self._stateRecorder.set_last_state(operation_type)  # i think this bit is a little shady (i will think of an alternative later)
            self._notify()

        else : print('Operation not allowed')


class Client(_ObserverInteface):

    def __init__(self, notifier:_ObservableInterface):
        self._notifier = notifier
        self._notifier._add(self)
        self._last_state = self._notifier._stateRecorder.get_last_state()

    def update(self):
        state_recorder:DatabaseStateRecorder = self._notifier._stateRecorder
        self._last_state = state_recorder.get_last_state()
        return self._last_state
    
    def get_data(self):
        return self._last_state


recorder = DatabaseStateRecorder()

src = DatabaseNotifier(recorder)

client1 = Client(src)
client2 = Client(src)
client3 = Client(src)

ass = ''

src.get_last_state()
src.remove(ass)
src.remove(client3)
src.operation('Delete')

client1.update()
client1.get_data()

recorder.get_last_state()
recorder.set_last_state('asd')
