# Cred Stuff

Usernames and passwords are matched by line number, so the password of `cultiris` is `cvpbPGS{P7e1S_54I35_71Z3}`
since both lines are from line 378 in their respective files.

The password is encrypted, but notice that `cvpbPGS{` in the password looks similar to `picoCTF{`. When
attempted a few different keys with the Caesar cipher decoder on https://www.boxentriq.com/code-breaking/caesar-cipher,
`key = 13` gives the desired flag `picoCTF{C7r1F_54V35_71M3}`.

<a href="https://play.picoctf.org/practice/challenge/261">Source</a>
