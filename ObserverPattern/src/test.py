from concrete import ObservableConcrete, ObserverConcrete

termo = ObservableConcrete()

client1 = ObserverConcrete(termo)
client2 = ObserverConcrete(termo)
client3 = ObserverConcrete(termo)
client4 = ObserverConcrete(termo)


termo.set_data('asd')
