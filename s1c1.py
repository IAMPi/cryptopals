#!/usr/bin/python

import binascii 
import base64

hexstring = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expectedoutput = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
hex2ascii = binascii.unhexlify(hexstring)

print "Converted from hex to ascii: " + hex2ascii

ascii2hex=base64.b64encode(hex2ascii)

print "converted from ascii to base64: " + ascii2hex


print  + ascii2hex ==expectedoutput