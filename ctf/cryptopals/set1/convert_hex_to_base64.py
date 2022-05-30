import base64


hex_string = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64_string = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def hex_to_base64(message: bytes) -> bytes:
    decoded_string = base64.b16decode(message, casefold=True)
    print(decoded_string)
    return base64.b64encode(decoded_string)

assert hex_to_base64(hex_string) == base64_string
print("Test pass!")
