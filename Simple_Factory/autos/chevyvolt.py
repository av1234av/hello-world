from .abs_auto import AbsAuto

class ChevyVolt(AbsAuto):

    def start(self):
        print('Chevy Volt Electric')

    def stop(self):
        print('Chevy Volt Shutting down')