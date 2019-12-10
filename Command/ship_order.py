from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand

class ShipOrder(AbsCommand, AbsOrderCommand):
    name = "ShipOrder"
    description = "Ship Order"

    def __init__(self, args):
        pass

    def execute(self):
        pass