import blockchain
import block
from flask import Flask
from flask import request

node = Flask(__name__)


this_node_transactions = []

@nodes.route('/transaction',methods=['POST'])
def transaction():
    if request.method == 'POST':
        message = request.get_json()
        this_node_transactions.append(message)

        return "Transaction added\n"