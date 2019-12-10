from .abs_auto import AbsAuto

class NullCar(AbsAuto):

    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('%s Undefined' % self._carname)

    def stop(self):
        pass