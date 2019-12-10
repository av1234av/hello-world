from Simple_Factory.autos.autofactory import AutoFactory

factory = AutoFactory()

for carname in 'ChevyVolt', 'FordFocus', 'Tesla':
    car = factory.create_instance(carname)
    car.start()
    car.stop()

