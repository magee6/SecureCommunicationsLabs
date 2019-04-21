import binascii

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

def egcd(a,b):                          # using extended euclidian algorithm to create rsa
    if a == 0:
        return(b, 0,1)
    g, y, x = egcd(b%a,a)
    return g, x - (b//a) * y,y

e = 65537
p = 163598797232837275790583032413921422452851861145478369331976309880028992955089558380171554447759405365296693377570783300198791468861355639873166150884714034914366548252757855530548966926710596087588892893653952147784119788340592861717511574050564549916735627066568966135368285851889401719649796310308064172229
q = 151928351783926490385254692544226090032004315756120674902384041799040568083955129227360764179393042678005292005933989750269377019057534023167675372696224003953154715102625798599561576746593076228704448522848509650863715575134525964992439285085243915010868628145127710442853766119688772555932018349278733467937

ciphertext = 4413233431418367729487001191499320110908628864393005850336194538378846901872012263024060279733910394528568658924541767014298273106072428208428621362441660742168169457839232452898840402021800460905562638079257404470183053387353849960252811956727755974787563684430128654542847575219444418360279725423441999278619584162289488016498634231451443666882615379215688913514242136494373656647328276909398980200846880640231426382657437148137610018777974884800967755913109702229247523206388812041488414941125272083962209616158810973532091497979384180936871075352614021504627549173686729322478688708849605857667792183339692021980


n = p * q                               # calculatee n by multiplying prime values for p and q
print ("n is : ",n)

phi = (p-1) * (q-1)                     # calculate totient value


gcd, a, b = egcd(e,phi)                 #modular inverse of e is calculated
d = a
decrypted = pow(ciphertext, d, n)
plaintext = int2string(decrypted)
print (plaintext)