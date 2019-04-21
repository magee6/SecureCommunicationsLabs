import hashlib

seed = "ecsc"                                       # seed for ECSC
hash_found = False                                  # hash_found set to False

challHash = 'c89aa2ffb9edcc6604005196b5f0e0e4'      # Challenge hash to be matched

hash = hashlib.md5()                                # an instance of the hashlib library is made
hash.update(seed.encode('UTF-8'))
seedHash = hash.hexdigest()                         # md5 hash of the seed is calculated
print("Seed Hash is",seedHash)                      # shows seed hash or the intital hash to be used

while  hash_found == False:
    if seedHash == challHash:                       # if the value of seedHash is the same as the challHash it will break out of the loop
        print("Hash Found:" + seedHash)
        break
    else:
        seedHash = hashlib.md5(seedHash.encode('UTF-8')).hexdigest()    # while hash_found is false it will continue to hash
        print(seedHash)








