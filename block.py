import hashlib
import random
import string
import datetime

class Block:
    def __init__(self, predecesure_hash, transaction):
        self.pre_hash = predecesure_hash
        self.salt = ''.join(random.choice(string.ascii_lowercase+string.digits) for i in range(6))
        self.transaction = transaction
        self.timestamp = str(datetime.datetime.now())
        self.target = 2**(256 - 20)
        self.breakSolve = False

    def setParams(self, prehash, transaction, salt, timestamp, thehash, nonce):
        base_str = self.pre_hash + timestamp + transaction + salt + str(nonce)
        if hashlib.sha256((base_str).encode('ascii')).hexdigest() == thehash:
            self.salt = salt
            self.timestamp = timestamp
            self.transaction = transaction
            self.hash = thehash
            self.nonce = nonce
            return True
        return False

    def solve(self):
        self.nonce = 0
        self.breakSolve = False
        base_str = self.pre_hash + self.timestamp + self.transaction + self.salt
        for nonce in range(2**32):
            print(nonce)
            hash = hashlib.sha256((base_str + str(nonce)).encode('ascii')).hexdigest()
            if int(hash, 16) < self.target:
                self.nonce = nonce
                self.hash = hash
                break
            if self.breakSolve:
                print("breaking solve")
                break
