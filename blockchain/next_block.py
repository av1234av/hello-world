import block
import datetime
def next_block(previous_block):
    this_index=previous_block.index + 1
    return block.Block(this_index,
                       datetime.datetime.now(),
                       'New block' + str(this_index),
                       previous_block.hash)