import hashlib

seed = "ecsc"
authenticate = False;

challHash = 'c89aa2ffb9edcc6604005196b5f0e0e4'

hash = hashlib.md5()
hash.update(seed.encode('UTF-8'))
seedHash = hash.hexdigest()
print("Seed Hash is",seedHash)

while authenticate == False:
    if seedHash == challHash:
        print("Hash Found:" + seedHash)
        authenticate == True
        break
    else:
        seedHash = hashlib.md5(seedHash.encode('UTF-8')).hexdigest()
        print(seedHash)








