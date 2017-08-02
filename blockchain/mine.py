import blockchain.blockchain
import block
from transaction import node
import datetime

from transaction import this_node_transactions
import json

my_address='xxxx-yyyyy-random-miners-address-99999'


def proof_of_work(last_proof):
    incrementor=last_proof + 1

    while incrementor % 7 == 0 and last_proof % 7 == 0:
        incrementor += 1

    return incrementor

@node.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain[len(blockchain) - 1]
    last_proof = last_block.data['proof-of-work']

    proof = proof_of_work(last_proof)

    this_node_transactions.append({'from':'Network','to':my_address,'amount':1})

    new_block_data = {'proof_of_work':proof,
                      'transactions':list(this_node_transactions)}
    new_block_index = last_block.index + 1
    new_block_timestamp = this_timestamp = datetime.datetime.now()
    last_block_hash = last_block.hash

    mined_block = block.Block(new_block_index,
                              new_block_timestamp,
                              new_block_data,
                              last_block_hash)

    this_node_transactions[:]=[]
    blockchain.blockchain.append(mined_block)

    return json.dumps({
        'index': new_block_index,
        'timestamp':str(new_block_timestamp),
        'data': new_block_data,
        'hash':last_block_hash
    })