from __future__ import print_function
import ast
from binascii import unhexlify
from secp256k1 import *
from utils import *
from termcolor import colored


"""
This implements AOS 1-out-of-n ring signature which require only `n+1`
scalars to validate in addition to the `n` public keys.

''Intuitively, this scheme is a ring of Schnorr signatures where each
challenge is taken from the previous step. Indeed, it is the Schnorr
signature scheme where n=1''

For more information, see:

 - https://www.iacr.org/cryptodb/archive/2002/ASIACRYPT/50/50.pdf

When verifying the ring only the initial seed value for `c` is provided
instead of supplying a value of `c` for each link in the ring. The hash
of the previous link is used as the next value of `c`.

The ring is successfully verified if the last value of `c` matches the
seed value.

For more information on turning this scheme into a linkable ring:

 - https://bitcointalk.org/index.php?topic=972541.msg10619684#msg10619684
 - https://eprint.iacr.org/2004/027.pdf

The Hacky version abuses the Ethereum `ecrecover` operator to perform
the Schnorr signature verifications.
"""


def hacky_schnorr_calc(xG, s, e, message):
	
	
	kG = hackymul(xG[0], xG[1], e, m=(((N - s) % N) * xG[0]) % N)
	#print(colored(kG,'red'))
	return hashs(xG[0], xG[1], bytes_to_int(unhexlify(kG)), message)


def haosring_randkeys(n=4):
	skeys = [randsn() for _ in range(0, n)]
	
	pkeys = [sbmul(sk) for sk in skeys]
	
	i = randint(0, n-1)
	return pkeys, (pkeys[i], skeys[i])


def haosring_sign(pkeys, mypair, tees=None, alpha=None, message=None):
	assert len(pkeys) > 0
	message = message or hashpn(*pkeys)
	mypk, mysk = mypair
	myidx = pkeys.index(mypk)

	tees = tees or [randsn() for _ in range(0, len(pkeys))]
	cees = [0 for _ in range(0, len(pkeys))]
	alpha = alpha or randsn()

	i = myidx
	n = 0
	while n < len(pkeys):
		idx = i % len(pkeys)
		c = alpha if n == 0 else cees[idx-1]
		
		cees[idx] = hacky_schnorr_calc(pkeys[idx], tees[idx], c, message)
		n += 1
		i += 1

	# Then close the ring, which proves we know the secret for one ring item
	# TODO: split into schnorr_alter
	alpha_gap = submodn(alpha, cees[myidx-1])
	tees[myidx] = addmodn(tees[myidx], mulmodn(mysk, alpha_gap))
	print(pkeys, tees, cees[-1])
	return pkeys, tees, cees[-1]


def convert_hex_to_int_pairs(hex_str):
     # split the input string into a list of hex strings
        hex_list = hex_str.split(',')

     # convert each hex string to an integer
        int_list = [int(hex_val, 16) for hex_val in hex_list]

        # group the integers into pairs
        int_pairs = [(int_list[i], int_list[i+1]) for i in range(0, len(int_list), 2)]
        print(int_pairs)
        return int_pairs

def haosring_check(pkeys, tees, seed, message=None):
	assert len(pkeys) > 0
	assert len(tees) == len(pkeys)
	message = message or hashpn(*pkeys)
	c = seed
	for i, pkey in enumerate(pkeys):
		c = hacky_schnorr_calc(pkey, tees[i], c, message)
	return c == seed

def hex_string_to_int_tuple(hex_str):
    hex_str_list = hex_str.split(',')
    int_tuple = tuple(int(x, 16) for x in hex_str_list)
    return int_tuple

def convertHexPubKeyToInt(_x,_y):
	x = int(_x,16)
	y = int(_y,16)
	return x,y

#exemple of use

# pkey = [(75435849508627179840796133162617517837963442917493453449174599455799962026794, 74182103438035685999104381890221198325436154553857252894063584672819063616159),(110786199081147917434273729123229780176651221213271254495027587441243752622128, 440567922157287245562649206244446874760093149384224012685677852470512153608), (83681620805307569183804693037600220117860210070056057158453379713897063750084, 105624771648380572404511236050440917521229213777114895671813240902974193710396), (53188094803348913103058365090030928935323179780535512152430250284636308030736, 59350247655223730134488201366610916430154113232018830184267269450865049361607), (89067375617973029214824807564419844247556672303528107077893590629417598875117, 10179398253299951489718810915948553861328337928134636523017703429393580106817), (13540864938875014518911691558042270735600051770836351949831361713697234675886, 50450542595583114535166580655300085031216524441980275622042658117183792669326), (37884512962717325989478589158672435020081076349246919356251696887303447419077, 89505016775626710852756529805476865557703846510446294422920634291311443829406), (74449860882734610219846850171166729821082999300063670915423523968714216216938, 2810927872056637651115401188966188331460331406060244114250649622742381521397), (20467868876146961732073031785291364654919879524457440319424237469570705864682, 95983597854081945924612492664054501307888906877866217713003146007107253563740), (30652476937640809831851309580488700156092129142960944114581403263636674641369, 95473466081194581092543470391193930065819756112270530182022309338672626359299), (103533568812631448651778543469676546549043515331930844988086911817925992900105, 70336794725089621720666086559327814902296552026231453513634965963502850317708), (57081694408547654376982552087908270236879461923059573161453549511394594855741, 23044935681823178924676008020054378239355302892926741248917977987842086896645), (53541360145032849045225156149275849566845924241257937334389442099551022172390, 105979096694234896976024905593671221501176561867400948399181558999868757067799)]
# mykey =[(110786199081147917434273729123229780176651221213271254495027587441243752622128, 440567922157287245562649206244446874760093149384224012685677852470512153608), 34398354710194674968351086021946151179232243894034636963607264492330427227051]
# message = int("0x9198aEf8f3019f064d0826eB9e07Fb07a3d3a4BD",16)
# proof = haosring_sign(pkeys=pkey,mypair=mykey,message=message)
# print(proof)
# print(haosring_check(*proof,message=message))
