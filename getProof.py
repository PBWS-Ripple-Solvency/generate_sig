import sys
from hackyaosring import haosring_sign
import requests
from get_data import getRing
from getPoints import getPoints
from mint_nft import mintNFT
import ipfsApi
#from ring_signature.hackyaosring import haosring_sign

# pkey = [(115185473299647925444517437276795129670496237591884117069305290769490785372619,77315467441032930729971643386403848327495819100754888420609510070437620990962),(69842940699001444947118319642196642553073776903718332284726491807873962548236,1127970563606141788355784463430840738461580530412738073901802949073783286569)]
# mykey =[(69842940699001444947118319642196642553073776903718332284726491807873962548236,1127970563606141788355784463430840738461580530412738073901802949073783286569),42071751069461095803574485567668923649610482576714143835877678793973757093411]
# message = int("0x9198aEf8f3019f064d0826eB9e07Fb07a3d3a4BD",16)
# proof = haosring_sign(pkeys=pkey,mypair=mykey,message=message)

def sendToIpfs(data):
    files = {
        'file': data
    }
    response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=('2NEFcw6jsQRonyXpWguSouymY4o',"588a638882fff36f65b8c0c76aef28ce"))
    a = response.json()
    return a['Hash']
def getProof(treshold, seedprivate, seedpublic):
    baseSet = getRing(treshold)
    points = getPoints(seedprivate)
    anonimtySet = [tup for tup in baseSet if tup[1] is not None]
    anonimtySet.append(points[0])
    print(anonimtySet)
    proof = haosring_sign(anonimtySet,points,message=12)
    hash = sendToIpfs(str(proof))
    print(hash)
    data = ('https://gateway.ipfs.io/ipfs/'+str(hash)).encode().hex()
    mintNFT(seedpublic,data=data)


     
