from xrpl.wallet import Wallet
import ecdsa
import math

p = 2**256 - 2**32 - 977

def getPoints(seed):
    issuer_wallet = Wallet(seed=seed, sequence=0)
    issuerAddr = issuer_wallet.classic_address
    issuersk = issuer_wallet.private_key[2:]   
    private_key_int = int(issuersk,16)
    num_bytes = math.ceil(private_key_int.bit_length() / 8)
    
    sk = ecdsa.SigningKey.from_string(private_key_int.to_bytes(num_bytes,byteorder='big'), curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    public_key = vk.to_string()
    print(len(public_key))
    x = int.from_bytes(public_key[0:32], byteorder='big')
    y = int.from_bytes(public_key[33:64],  byteorder='big')
    return[(x,y),int(issuersk,16)]
   
