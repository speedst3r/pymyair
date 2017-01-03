from Crypto.Cipher import AES
from Crypto import Random
import binascii, base64

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        """
        Returns hex encoded encrypted value!
        """
        raw = pad(raw)
        iv = Random.new().read(AES.block_size);
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return ( iv + cipher.encrypt( raw ) ).encode("hex")

    def decrypt( self, enc ):
        iv =  str(bytearray(16))
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc))

def swap(s, i, j):
    return ''.join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]))

if __name__== "__main__":
    key = "UM0jQuPL1b5+uNjU+O+vtw0UGTN+JwFk"
    key = swap(key, 3, 27)
    key = swap(key, 9, 17)
    #key = key.encode("hex")
    ciphertext = "/RP0v9OPPc0tyAX3D8bRuQM1hq1-xvvqR3oJWyfUPiNI=-"
    ciphertext = ciphertext[1:] # skip /
    #key=key[:32]
    decryptor = AESCipher(key)

    if ciphertext[-1] == '-':
        decode = base64.urlsafe_b64decode(ciphertext[:-1])
        obj = 1
    else:
        decode = base64.b64decode(ciphertext[:-1])
        obj = 0
    final = decryptor.decrypt(decode)
    if obj == 0:
        plaintext = final
    else:
        plaintext = final[3:]
    print("%s" % plaintext)