import M2Crypto
import os
import re
from base64 import b64encode, b64decode

# this is your keypair, private and public
class RSAKeypair:

    def __init__(self, m2crypto_keypair=None, public_pem=None, private_pem=None):
        self._m2crypto_keypair = None

        if m2crypto_keypair is not None:
            self._m2crypto_keypair = m2crypto_keypair            

    @classmethod
    def generate(cls, size=4096):
        rand_seed()

        # 65537 is a good exponent to use according to wikipedia
        new_key = M2Crypto.RSA.gen_key (size, 65537, empty_callback)
            
        return RSAKeypair(m2crypto_keypair=new_key)

    @classmethod
    def from_file(cls, filename):
        return RSAKeypair(m2crypto_keypair=M2Crypto.load_key(filename))

    # synonym for from_file
    @classmethod
    def load(self, filename):
        return RSAKeypair.from_file(filename)

    @classmethod
    def from_pem(cls, pem_string):
        pem_string = re.sub("\n?-----(BEGIN|END) RSA (PUBLIC|PRIVATE) KEY-----\n", '', pem_string)

        return RSAKeypair(m2crypto_keypair=M2Crypto.load_key_string(pem_string, callback=empty_callback))


    def private_pem(self):
        return self._m2crypto_keypair.as_pem(callback=empty_callback, cipher=None)

    def __public_bio(self):
        bio = M2Crypto.BIO.MemoryBuffer()
        self._m2crypto_keypair.save_pub_key_bio(bio)
        return bio

    def public_pem(self):
        return self.__public_bio().read_all()

    def public_key(self):
        return RSAPublicKey(m2crypto_key=M2Crypto.RSA.load_pub_key_bio(self.__public_bio()))
    
    def save_private_pem(self, filename):
        self._m2crypto_keypair.save_key(filename, callback=empty_callback, cipher=None)

    def save_public_pem(self, filename):
        self._m2crypto_keypair.save_pub_key(filename)

    # will save filename_base and filename_base.pub
    def save(self, filename_base):
        self.save_private_pem(filename_base)
        self.save_public_pem(filename_base + '.pub')

    def decrypt(self, message):
        return self._m2crypto_keypair.private_decrypt(message, M2Crypto.RSA.pkcs1_oaep_padding)

    def generate_signature(self, encrypted_message):
        message_digest = M2Crypto.EVP.MessageDigest ('sha1')
        message_digest.update (encrypted_message)

        return self._m2crypto_keypair.sign_rsassa_pss (message_digest.digest())
        

# use this for another user you'd be interacting with (someone who's public key you'd have)
class RSAPublicKey:
    
    def __init__(self, m2crypto_key=None):
        self._m2crypto_key = None

        if m2crypto_key is not None:
            self._m2crypto_key = m2crypto_key

    @classmethod
    def from_file(cls, filename):
        return RSAPublicKey(m2crypto_key=M2Crypto.RSA.load_pub_key(filename, callback=empty_callback))

    # synonym for from_file
    @classmethod
    def load(cls, filename):
        return RSAPublicKey.from_file(filename)
    
                            
    @classmethod
    def from_pem(cls, pem_string):
        pem_string = re.sub("\n?-----(BEGIN|END) RSA PUBLIC KEY-----\n", '', pem_string)
        
        bio = M2Crypto.BIO.MemoryBuffer(data=pem_string)

        return RSAPublicKey(m2crypto_key=M2Crypto.RSA.load_pub_key_bio(bio))

    def encrypt(self, message, base64_encode=False):
        rand_seed()

        return self._m2crypto_key.public_encrypt(message, M2Crypto.RSA.pkcs1_oaep_padding)

    def __public_bio(self):
        bio = M2Crypto.BIO.MemoryBuffer()
        self._m2crypto_keypair.save_pub_key_bio(bio)
        return bio

    def pem(self):
        return self.__public_bio().read_all()

    def verify_signature(self, encrypted_message, signature):
        message_digest = M2Crypto.EVP.MessageDigest ('sha1')
        message_digest.update(encrypted_message)
        
        return (self._m2crypto_key.verify_rsassa_pss (message_digest.digest(), signature) == 1)
        
        
        

def rand_seed():
    M2Crypto.Rand.rand_seed (os.urandom (1024))

# needed to override the stupid default callback M2Crypto uses for key generation
# that prompts for a password
def empty_callback(unused_arg=None):
    pass

