
from web3.middleware import geth_poa_middleware
from web3 import Web3
rpc_url = "https://polygon-testnet.public.blastapi.io"
bsd = Web3(Web3.HTTPProvider(rpc_url))

my_address = '0x8D736A5Bc12908C921BFEc525c5203C7f713Fa9E'
you_address = '0x4Ba760E5361cf7c9031698ea6dF979a9e989e869'


bsd.middleware_onion.inject(geth_poa_middleware, layer=0)
bsd.eth.account.enable_unaudited_hdwallet_features()


MNEMONIC = 'token devote either act original purse dignity laptop portion suggest rocket call'

account = bsd.eth.account.from_mnemonic(MNEMONIC)
private_key = account._private_key



def build_txn(
        *,
        web3: Web3,
        from_address: str,
        to_address: str,
        amount: float,
) -> dict[str, int | str]:

    gas_price = web3.eth.gas_price


    gas = 2_000_000

    nonce = web3.eth.get_transaction_count(from_address)

    txn = {
        'chainId': web3.eth.chain_id,
        'from': from_address,
        'to': to_address,
        'value': int(Web3.to_wei(amount, 'ether')),
        'nonce': nonce,
        'gasPrice': gas_price,
        'gas': gas,
    }
    return txn


transaction = build_txn(
    web3=bsd,
    from_address=my_address,
    to_address=you_address,
    amount=0.333,
)


signed_txn = bsd.eth.account.sign_transaction(transaction, private_key)


txn_hash = bsd.eth.send_raw_transaction(signed_txn.rawTransaction)


print(txn_hash.hex())