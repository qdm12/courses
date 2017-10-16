#/usr/bin/python3

# Requires base58 and ecdsa

from ecdsa.ecdsa import Public_key as generate_publicKey, generator_secp256k1 as G, int_to_string
import hashlib
from base58 import b58encode, b58decode
from random import randint
from time import time
import multiprocessing

def b58encodecheck_address(address):
    return b58encode(b'\x6f' + address + sha256(sha256(address))[0:4])

def b58decodecheck_address(address):
    return b58decode(address)[1:-4]

def b58encodecheck_privateKey(secret, compressed = False):
    privateKey = b'\xef' + secret
    if compressed:
        privateKey += b'\x01'
    privateKey += sha256(sha256(privateKey))[0:4]
    return b58encode(privateKey)
    
def b58decodecheck_privateKey(privateKey):
    if isCompressed(privateKey):
        return privateKey[1:-5]
    else:
        return privateKey[1:-4]
        
def isCompressed(privateKey):
    if privateKey[-4:] == sha256(sha256(bytes.fromhex(privateKey[:-4].hex())))[0:4]:
        if len(privateKey[:-4]) == 34 and privateKey[-5:-4] == b'\x01':
            return True
        elif len(privateKey[:-4]) == 33:
            return False
        else:
            raise Exception("Private key has the wrong length.")
    else:
        raise Exception("Private key is corrupted as the checksum is wrong.")

def calculate_address(public_key):
    address = hash_160(public_key) # in byte format
    return b58encodecheck_address(address)

def sha256(data):
    return hashlib.sha256(data).digest()

def hash_160(data):
    hashA = sha256(data)
    hashB = hashlib.new('ripemd160', hashA).digest()
    return hashB

def generate_keys(secretNumber):
    private_key_bytes = int_to_string(secretNumber)
    private_key_hex = private_key_bytes.hex().upper()
    private_key_b58 = b58encodecheck_privateKey(bytes.fromhex(private_key_hex))

    public_key = generate_publicKey(G, G*secretNumber)
    public_key_bytes = b'\x04' + int_to_string(public_key.point.x()) + int_to_string(public_key.point.y())
    public_key_hex = public_key_bytes.hex().upper()
    
    bitcoin_address = calculate_address(public_key_bytes)    

    return private_key_b58, public_key_hex, bitcoin_address 

def find_vanity_address(prefix, core, quitEvent, foundEvent):
    print("Vanity Address worker on core",core,"started")
    start = time()
    n = len(prefix)
    secret = randint(0, pow(2,256))
    point = G*secret
    i = 1
    temp = time()
    while not quitEvent.is_set():
        public_key = generate_publicKey(G, point)
        public_key_bytes = b'\x04' + int_to_string(public_key.point.x()) + int_to_string(public_key.point.y())
        address = calculate_address(public_key_bytes)
        if address[1:n+1] == prefix:
            private_key_bytes = int_to_string(secret + i)
            private_key_hex = private_key_bytes.hex()
            public_key_hex = public_key_bytes.hex()
            print("Found in",time()-start,"seconds")
            print("Private key:", private_key_hex)
            print("Public key:", public_key_hex)
            print("Address:", address)
            foundEvent.set()
            break
        if i % 500 == 0:
            print("Speed of worker on core", core, ":", 500 / (time() - temp), " addresses per second")
            temp = time() 
        i += 1
        point *= 2
        
def parallel_vanity_finder():
    quitEvent = multiprocessing.Event()
    foundEvent = multiprocessing.Event()
    for core in range(multiprocessing.cpu_count()-1):
        p = multiprocessing.Process(target=find_vanity_address, args=("abc", core, quitEvent, foundEvent))
        p.start()
    foundEvent.wait()
    quitEvent.set()    

def privateKey2Address(private_key):
    if len(private_key) in (51, 52):
        print("Private key is assumed to be in base58 check already.")
    elif len(private_key) == 64:
        print("Private key is assumed to be in hexadecimal, without check encoding.")
        private_key = b58encodecheck_privateKey(bytes.fromhex(private_key))
    elif len(private_key) == 74:
        print("Private key is assumed to be in hexadecimal, with check encoding.")
        private_key = b58encode(bytes.fromhex(private_key))
    elif len(private_key) in (37, 38):
        print("Private key is assumed to be in bytes, with check encoding.")
        private_key = b58encode(private_key)
    elif len(private_key) == 32:
        print("Private key is assumed to be in bytes, without check encoding.")
        private_key = b58encodecheck_privateKey(private_key)
    else:
        raise Exception("Private key is in an unknow format !")
    print("Private key in base 58 check is:", private_key)
    private_key = b58decode(private_key)
    secretBytes = b58decodecheck_privateKey(private_key)
    secretHex = secretBytes.hex()
    secretNumber = int(secretHex, 16)
    _, public, address = generate_keys(secretNumber)
    print("Public key: ", public)
    print("Address: ", address)

if __name__ == "__main__":
    privateKey2Address('cTgPHgYsLYRBeHUC8z2gmpXtPuvzSF8A6fRrest2kK45gQBoxDUU')
    # print(generate_keys(randint(0,pow(2,256))))
    #parallel_vanity_finder()
