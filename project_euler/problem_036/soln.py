result = 0
for i in range(1, 1000000):
    num_str = str(i)
    if num_str[-1] == "0":
        continue
    if num_str != num_str[::-1]:
        continue
    bin_str = str(bin(i))[2:]
    if bin_str[-1] == "0":
        continue
    if bin_str != bin_str[::-1]:
        continue
    result += i
print(result)
