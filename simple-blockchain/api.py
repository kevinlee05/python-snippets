from uuid import uuid4
from textwrap import dedent
from flask import Flask, jsonify, request
from .blockchain import Blockchain

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique (random) address (name) for this node
node_identifier = str(uuid4()).replace('-', '')

#instantiate the Blockchain
blockchain = Blockchain()

#Create the /mine endpoint, which is a GET request.
@app.route('/mine', methods=['GET'])
def mine():
    #we run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    return "We'll mine a new Block"

#Create the /transactions/new endpoint, which is a POST request, since we’ll be sending data to it.
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    #check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    #Create a new Transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block{index}'}
    return jsonify(response), 201

#Create the /chain endpoint, which returns the full Blockchain.
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


#Runs the server on port 5000.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
