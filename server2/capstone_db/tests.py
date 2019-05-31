
from web3 import Web3, HTTPProvider
import hashlib
rpc_url = "http://localhost:8545"
w3 = Web3(HTTPProvider(rpc_url))

def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()


path='./media/Love Dog.png'
print(sha256_checksum(path))

