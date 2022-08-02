#!/bin/bash
openssl aes-128-ecb -d -a -in 7.txt -K  $(echo -n "YELLOW SUBMARINE" | hexdump -v -e '/1 "%02X"')
