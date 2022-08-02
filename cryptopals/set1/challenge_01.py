# Convert hex to base64
# https://cryptopals.com/sets/1/challenges/1

import base64


hex_string = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64_string = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

decoded_hex_string = base64.b16decode(hex_string, casefold=True)
print(decoded_hex_string)
assert base64.b64encode(decoded_hex_string) == base64_string
print("Test pass!")

