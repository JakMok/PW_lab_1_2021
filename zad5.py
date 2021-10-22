def bin_length(number):
    return len(bin(number)) - 2


print(bin_length(12))
print(bin_length(1))
print(bin_length(1025))
