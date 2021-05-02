from databaseNotificationBase import Client, DatabaseNotifier, DatabaseStateRecorder




recorder = DatabaseStateRecorder()

src = DatabaseNotifier(recorder)

client1 = Client(src)
client2 = Client(src)
client3 = Client(src)

asss = ''

src.get_last_state()
src.remove(asss)
src.remove(client3)
src.operation('Delete')

client1.update()
client1.get_data()

recorder.get_last_state()
recorder.set_last_state('asd')
