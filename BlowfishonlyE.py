from Crypto.Cipher import Blowfish
from Crypto import Random
import base64


def Encrypt(msg):
 key = Random.new().read(16) 
 block_size = Blowfish.block_size

 iv = Random.new().read(Blowfish.block_size)
 padding = "$"
 p = lambda s:s + (block_size - len(s) % block_size )* padding
 c = Blowfish.new(key, Blowfish.MODE_CBC, iv)
 Encrypted_message = iv + c.encrypt(p(msg).encode('ascii'))
 return {key, base64.b64encode(Encrypted_message)}