import hashlib

h = hashlib.new('sha256')
h.update("Hello bitch".encode('ascii'))
hex = h.hexdigest()
print(hex)

while True:
    user_input = input()
    th = hashlib.new('sha256')
    th.update(user_input.encode('ascii'))
    hexoutput = th.hexdigest()

    if hexoutput == hex:
        print("correct")
    else:
        print("wrong")

    print(hexoutput)
