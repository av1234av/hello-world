from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand

class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = "UpdateQuantity"
    description = "Update Quantity Number"

    def __init__(self, args):
        self.newqty = args[1]

    def execute(self):
        oldqty = 5
        print ("updated database")

        print('Logging: Updated quantity from %s to %s' % (oldqty, self.newqty))
