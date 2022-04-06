import hashlib

message = input()
target = 2 ** (256 - 20)

for nonce in range(2**32):
    print(nonce)
    hash_result = hashlib.sha256((message + str(nonce)).encode('ascii')).hexdigest()

    if int(hash_result, 16) < target:
        print("success")
        print(hash_result)
        break
