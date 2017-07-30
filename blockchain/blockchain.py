import genesis
import next_block

blockchain = [genesis.genesis_block()]

previous_block = blockchain[0]

num_blocks_to_add = 20

if __name__ == '__main__':

    for i in range(0, num_blocks_to_add):
        block_to_add = next_block.next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        print "Block {0} added to the blockchain".format(block_to_add.index)
        print "Hash {0}".format(block_to_add.hash)