simplersa
=========

simplersa is a simple wrapper for M2Crypto designed to make basic encryption functionality, namely, key generation, encrypt, decrypt, signature generation, and signature verification, a little more straightforward.  An example:

	  Python 2.7.2 (default, Nov 21 2011, 17:25:27) 
	  [GCC 4.6.2] on linux2
	  Type "help", "copyright", "credits" or "license" for more information.
	  >>> 
	  >>> 
	  >>> from simplersa import RSAKeypair, RSAPublicKey
	  >>> 
	  >>> 
	  >>> 

Generate two private/public keypairs

	  >>> macho_man = RSAKeypair.generate()
	  >>> hulk_hogan = RSAKeypair.generate()
	  >>> 
	  >>> 

Now say Macho Man and Hulk Hogan want to exchange their public keys

	  >>> macho_man_public_pem = macho_man.public_pem()
	  >>> macho_man_public_pem
	  '-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA4yBg7nHHFYpipjuWW0mw\n3iLCnZ16tpgLssY2DWW/uDIuMN2BpCZnaUKSe+cIoR/3q9hDUhO+Q3ANrDi/tI3B\n0SXKlTi2SdCQmnzJ+HpACnJ82TUlpRl2prf21OXumxT6mnd55FHimaM/D8yekHmn\nR9waNEGZt2lZoF/zX0diriOlLWTrjh/inRipryH4CrvI+YILtcXxWRSnA97nmC2E\n5luAdeg8iZlxdkfmHDWlI9WbThjP5ATgga5K6WaWpfQTd85r94s0EhGKArVpts79\npQIi5COweuZ5FPR07VMZk8pv8PLmO8iTmuPq6faOwkWZqLer/7UUeLBOnEMaxUf7\nEMvgVDycD1He32OKoUuFaHivbMRKddGx+04vJEr1PYIQ+S5ZmReLsKjSynpFK/JU\n801YlmVmugK7pk1j9B93nlS2AWGkbQra0Lz9ICelxH8fTUxoWCRypKZ7TZW4TT+i\nv8UTRT5EYfIHp3hEe64s+k+plxJ40T3BPrl+tMUf1SYUyKYlGXepGVL7Sl0dLNhF\n3vSlI4Nh8KGMRuPHsec74cWuWq4DDm6dKYtz5ZewlLUqVQ0IWFhIToJa63pXbLEi\nq6FN+/0MCOE7qAVU2zphwu3xl+D/18g+CAsxELD2kH2MAOQjgCmQLQUljkWkih1x\nbIXmcm9fmhs9zENSz07kKm0CAwEAAQ==\n-----END PUBLIC KEY-----\n'
	  >>> 
	  >>> macho_man_public_key = RSAPublicKey.from_pem(macho_man_public_pem)
	  >>> 
	  >>> hulk_hogan_public_pem = hulk_hogan.public_pem()
	  >>> hulk_hogan_public_pem
	  '-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAyjzXUxAtEgxegP6nefAh\nb5q/QGt8Oo+RaMS1/jzQsZTTcwZPqAJh8I0pBI2yTCf/gYCrRc0j4XlsVkozz+w0\nEe1WkrbdwsKFmoUB7qusiCXu75kQ+PcIPm4go8VX0knAAAS4mBcbELuvVTuVj7sB\n1rmc10MK0IKK4gnZ1ePTpZ9foY0GrmSqZhAuzJNyY5OeS0U5uDKtGodB2H2s2YK8\n0BnoTeex7tv9UqWbvmfbU2aZxD29gpvVyxxf6yTcrKMC3l/PPNL1WW/MtFA/7aTk\nky6odTNhQyy+5z5icBNc7iwRgP6ygnoqzLTVeLkOcCRKHQzIHG8hSj7gKSe4CIGR\nt5lXnhSFW1B7IG7o7cu97SHKzravKUg2JQTwqKF4garjgdV74j8xL33MGYE+Yt8F\nQCz310dhReYVhHLRmubWO/03KmUbkSSKnxp75ysQzKYid0YgMq4swR9wz8iyetwf\ncGJBg4PGGqFykca3rw3oKpyiLy8E1SGLW450u+bPHwBq6O+gfyvIEwwsccUpaILQ\nmTGTko0fsD20u1sy9wtWrvoISLJ0VM4qHPocBZICmq0h9i0lXdIQtFJQ7W9s2lib\nfgeqjkw4Cy0qLvZ9tpTkDfhsOoN4/2PtL1Lk9Ek+87BBo965zvwrCqwHDxsZXSPr\nKkNVci+ustK2/AdBRFKQ3jMCAwEAAQ==\n-----END PUBLIC KEY-----\n'
	  >>> 
	  >>> 
	  >>> hulk_hogan_public_key = RSAPublicKey.from_pem(hulk_hogan_public_pem)
	  >>> 

Macho Man can now use Hulk Hogan's public key to encrypt a message

	  >>> 
	  >>> encrypted_message = hulk_hogan_public_key.encrypt("YOU'RE GOING DOWN, HOGAN!!!")
	  >>> encrypted_message
	  '?\xc2\xafi\xc3~\x15\x8b\xdc\x1d5\'\x92=X=\x06\xa0\xaa\x94\x87[\xd5%95\x1d\xdb\xf6\xe5\xf0;\x9c\xc7d\x18cL\x91\x8e[tA\xf2\xd2\xe2\xa7\\\x12m&\xbd\xe7.\x8c\'!\xe0w\xf0\xd2\xa7\x86[d\xb1\xd3\xe4o\xda+\x8e\x93\xb6\x98\x93\xfb\xfd\x04\x1b\xd8\xc3\x94`\xbdj\xfc\xb6\xa0E+\xa8\xe1\xfb\xd4\xc1h$c\xb0(x,\xd5\xe4\xc8\x82\xbeA\xd0\xa3!\x08|\x06\xb18\xe2\x85\xb5Z\x03)\xe0\x18-\x97]\x0cy7\xcd\xee\x12k\xed\xca\xb9s<G%\xe2;(Ak\x98%\xda`\x18\x1f&\xec\x19\xa39oV\xe2\x17\xbe\xbb\xe1\r\xf5l!\xcf\x85\xb9\xdd\xca\x04\x03@\x89u5\'a\xdfw>\xd4\xaa\x0e?\xcd\xbd?\xe4\xd7\xae\xe4R%\t\x07D\xd1d\x868\x85\xae<\x8d\xadnL0i\x06b\xdbPA\xf1\xa3\x15\x80\x9d5@]\x8cp\x11\xe7\x15\xb8y\xfe<\xc6\xff\x0c\xc0\x11C|\xf3S\xd5Z\xe9\xbb \xd39\xc5Y\x90\xb9C&*\xcb\r\xe2&\x86\xff\xf5"\x97x\xb4\x0f\x9b\x9bkwd|\x90K%\xcc\xfcX.\xd2f\xb5\xf7.>\x1enw\tp\xf9G\xe1\xb3\x04n\x7f\xe6\xfe2\xf4>\x04\xee 5`r\x80\xd1\xb7\x88\xb1\x96B>=\xb5Q\x96\xee\xc3\xaaNQ\xc2\x872\x85Vt\x8d}:\xb4\xff.\xfe1\x80.\xcd\xa2\x86\xf5N\xffZ\xbb\xb7\x0e\xfaI\x9a\xee\xfa\xac\xa1\xdd\x17\xe1\x99n\x80\xe9\xef\x91\xcc\xb1\xaa\t\xea\xe4.<I7P\x05\xf9\xf9>A}R\x8b\xeah.5\x86)5\xe1\x1e\x86k[\x0es\x16\xa2\xa8{\x0c\x97\x0cg\x05\xab\x9e\x13\xe0\x1799`\x8f\xf9\xb0\x90\x15s\xde\xa8\xc5\xa8\xa7\x04O\xa3\x15Z\xaf|\x8dW\x1d\xab\xe3\x1b|\xe3\x82\xc8\x00\xa5\xed\xbb#Y\xf0\x89\x90g\x1e\x07\x10R\xfau\x91\xcfr\xfe\xaf2\xc9\x02\xb1\xb1\nr\x1a\x9c|\xaa\xa9\xfe\xbc\x86El\xc1\x83\xdb\x97\xb1\xd0\xb0/\xd2\x0c\xd7\xa4H{\x02\x85\x99\xcfk\xfb[\xd3\x93\x8f'
	  >>> 
	  >>> 

and use his own private key to generate a signature for said message

	  >>> signature = macho_man.generate_signature(encrypted_message)
	  >>> signature
	  '\xdd\xcdd\x91>Yul\x8e\xc9\x0c\xef\xb8\x03\xbfq\xf9\xcd\xcd\x8a\xdd\x1e\xc7\x9f\x81\xa6\x9a\xd8}\x83\xca\x05{caR8\x1a\xee\x0c\x0e\x05\xce\xa0\xa6\x0cD\x8c/mJ~\xd1\xbfZ#\xa6W\x8a\xa29\x99q\xa5c8\xeb\x1e+\xbe\xa7M0\xa9\xe4$|FY\x03\x90\x0e\xa8\xd4\xfb\x00\xf3\xa4\x80\xcc\xa5&,\x9c\xaa1j\xb14\xb2BZ\\be{\xb4F\x9bo\xa0\xa3q\xa7t`\xa5\xd7j\xe6gd\xcdTK8T\x11\x00\x19\xf1\xa5\x9a\xc9\xd2\xd7\x84N\xc0\\\xc8uI\xf7\xc0\x9f\xde~\xd2\xe4Dh\x19\xe0\xe1gQ#0\x95\xc6\xde\xc9\xac\x8b\xb3\xf2?~f\x9c\x0e\x19\x9e\xa2\x0co\xf8\xe2X\xc37n\xea\x02\x18\xc1k\xf2{:\x96\xdb\xe8\r\x02\x84\x0bz\x14*\xd2-\x1c\xc2"\x19\xdbVL=\xd2ER\x06!P\xfe\x8fR9\xb6\xbc\t\'\x1fNG\xdc#F\xd9\xf1\xc1\x97*\x1d\x89\xaa\xa7}$\xa5\xd9\xbbX\xe7wO8\xa4\xd2\xaf\xacM\xf6\xdf|K;\xb6%,?\x10*\x9c\x03\x99\x9f?6\x83z\xa6\x9e\x97\xa7\xbf\xb8\xff65-\x04\x87G\x10\x9c\xc9@\x81\xb1\x0c|\x7fo\x9e\xa6Hz\xf9D\xc7\x01bE"\x1cx\xddm\x9e=\xee\xe9\xba\x921n\xb2 ~R S,*?\xc6|\xf4\xad\x13#\xb34\x06\x13O\xe8\xead3{\xa7\xec\x9a\xa8NQ\xa0\xec\x96\xd0\x8fY\xd0\x90\x13B\x1an\xcf\xf5\x82{\xb1\xe4\xae\xd6\x8e\xfd\x03\x7f\xc5\xed\xc3\xae8[\x107\\|\xc6#\xd3\x89Ur\x96\x1f\xb1\xa6\xcb\x9c\xdf\x8d\x87f\x9b\xbc\x17\xe2\xc9\x1e\xd5Z%\xb0\xb2\x8c\xf6p*\xc1\x19\x8a*\xae\xf5\xe2\xec\x19\xb1\xe7\x83\xabn\xbb0\'W0\'\\[;V"\xbb\x86\xb4\xcae\xa9!\x83B\xf66\xdb\xc3.\x9c\xd0.\xdf\x03\'\x01xl\x17\xc7\xea}\xfb\'\x8a\xa4\xa7\x1f\xee\xa5\x9amWm\xc3\x04\xaf\x95\xb7\x05\xe7\xc9s\xee\xe0\x84\xac+>\xcaK\xb1\x01\xff\'VV\xfa#b\xeb\xfd;\xba\xa0a'
	  >>> 

The encrypted message can now be sent to Hulk Hogan, who can use his own private key to decrypt the message

	  >>> decrypted_message = hulk_hogan.decrypt(encrypted_message)
	  >>> 
	  >>> 
	  >>> decrypted_message
	  "YOU'RE GOING DOWN, HOGAN!!!"
	  >>> 

and use Macho Man's public key to verify the signature

	  >>> 
	  >>> macho_man_public_key.verify_signature(encrypted_message, signature)
	  True

RSAPublicKey also has a couple of instance methods for things like loading from disk (*load(filename)*), saving to disk (*save(filename)*, which will save filename and filename.pub), and class methods for things like loading from a pem string (from_pem()).  
