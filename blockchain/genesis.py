import block
import datetime as date
def genesis_block():
    return block.Block(0,date.datetime.now(),'genesis block',"0")