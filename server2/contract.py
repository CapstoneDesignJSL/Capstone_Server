import web3
import time
from web3 import Web3, HTTPProvider
from solc import compile_files


# INS  = deploy()
rpc_url = "http://localhost:8545"
w3 = Web3(HTTPProvider(rpc_url))
# w3 = Web3(IPCProvider("./chain-data/geth.ipc"))
w3.personal.unlockAccount(w3.eth.accounts[0], "admin", 0)

def deploy(contract_file_name, contract_name):

    compiled_sol = compile_files([contract_file_name])
    interface = compiled_sol['{}:{}'.format(contract_file_name,
                                            contract_name)]

    contract = w3.eth.contract(abi=interface['abi'],
                               bytecode=interface['bin'],
                               bytecode_runtime=interface['bin-runtime'])

    # Deploy
    tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0]})
    # print(tx_hash)
    # logger.info("tx_hash: {}".format(tx_hash))

    # Mining
    w3.miner.start(2)
    time.sleep(5)
    w3.miner.stop()

    # Contract address
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    print(tx_hash)
    contract_address = tx_receipt['contractAddress']
    # logger.info("contract_address: {}".format(contract_address))
    # Use contract
    contract_instance = contract(contract_address)
    return contract_instance
