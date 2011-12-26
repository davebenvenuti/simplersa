from distutils.core import setup
setup(name='simplersa',
      version='0.1',
      py_modules=['simplersa'],
      author='Dave Benvenuti',
      author_email='davebenvenuti@gmail.com',
      description="A simple wrapper for M2Crypto's RSA functionality",
      requires=["M2Crypto"]
      )
