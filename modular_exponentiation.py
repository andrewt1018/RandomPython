def mod_exp(num, exp, mod):
    bin_exp = str(bin(exp))[2:][::-1]
    modded_chain = 1
    counter = 0
    for char in bin_exp:
        if char == '0':
            counter += 1
            continue
        elif char == '1':
            modded_chain *= (num ** (2 ** counter)) % mod
            counter += 1
    return modded_chain % mod

def mod_exp2(num, exp, mod):
    x = 1
    bin_exp = str(bin(exp))[2:]
    power = num % mod
    for i in range(0, len(bin_exp)):
        if bin_exp[i:i+1] == '1':
            x = (x * power) % mod
        power = (power * power) % mod
    return x

# Testing on 572 ^ 29 mod 713
print(mod_exp(572, 29, 713))

