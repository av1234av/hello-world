from transaction import node
import blockchain
import json
from flask import Flask, request

@node.route('/blocks',['GET'])
def get_blocks():
    # convert blocks to dict

    chain_to_send = blockchain.blockchain[]
    for block in chain_to_send:
        block = {"index":str(block.index),
                 "timestamp":str(block.timestamp),
                 "data":str(block.data),
                 "hash":block.hash}

    chain_to_send = json.dumps(chain_to_send)
    return chain_to_send

def find_new_chains(peer_nodes):
    other_chains=[]

    for node_url in  peer_nodes:
        block =