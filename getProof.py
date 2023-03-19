import sys
from hackyaosring import haosring_sign

from get_data import getRing
from getPoints import getPoints
from mint_nft import mintNFT
#from ring_signature.hackyaosring import haosring_sign

# pkey = [(115185473299647925444517437276795129670496237591884117069305290769490785372619,77315467441032930729971643386403848327495819100754888420609510070437620990962),(69842940699001444947118319642196642553073776903718332284726491807873962548236,1127970563606141788355784463430840738461580530412738073901802949073783286569)]
# mykey =[(69842940699001444947118319642196642553073776903718332284726491807873962548236,1127970563606141788355784463430840738461580530412738073901802949073783286569),42071751069461095803574485567668923649610482576714143835877678793973757093411]
# message = int("0x9198aEf8f3019f064d0826eB9e07Fb07a3d3a4BD",16)
# proof = haosring_sign(pkeys=pkey,mypair=mykey,message=message)

def getProof(treshold, seedprivate, seedpublic):
    baseSet = getRing(treshold)
    points = getPoints(seedprivate)
    anonimtySet = [tup for tup in baseSet if tup[1] is not None]
    anonimtySet.append(points[0])
    print(anonimtySet)
    proof = haosring_sign(anonimtySet,points,message=12)
    data = str(proof).encode('utf-8').hex()
    print(data)
    mintNFT(seedpublic,data=data)

getProof(5, "sEdTyvTbcKrQCvNcZ9fdUfvL4MMYE3Q","sEdVb34TB7AWkLcVCiyQMbT2WKqi5B8")
     
