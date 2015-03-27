'''
Hash generator
'''
import hashlib

def gen_hash(text, method="ripemd160"):
    '''
    Generate Hash
    '''
    rmd160 = hashlib.new(method)
    rmd160.update(text.encode())
    return rmd160.hexdigest()
