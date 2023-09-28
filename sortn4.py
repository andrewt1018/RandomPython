def sort_nToP(array: list, n, p) -> list:
    # Function to sort an array of n elements all within the range of 1 to n^p in O(n)
    l = len(array)
    new_array = []
    for i in range(0, l): # Conversion takes O(n)
        converted = convert_base(array[i], 10, n, 4)
        new_array.append(converted)
    
    print("Base_n array:", str(new_array))
    
    for j in range(0, p): 
        new_array = count_sort(new_array, j)
    
    ret = []
    for i in new_array:
        # ret.append(convert_to_decimal(i, n, p))
        ret.append(convert_base(i, n, 10, 4))
    return ret

        
def count_sort(array, digit):
    # Count sort for an array of numbers for a specific digit (radix sort)
    c = []
    for i in range(10):
        c.append(0)

    n = len(array)
    b = []
    for i in range(n):
        b.append(0)

    for i in range(n):
        num = array[i]
        value = num // (10 ** digit) % 10
        c[value] = c[value] + 1
        
    for i in range(1, 10):
        c[i] = c[i] + c[i-1]
    
    for i in range(n-1, -1, -1):
        num = array[i]
        value = num // (10 ** digit) % 10
        b[c[value] - 1] = num
        c[value] = c[value] - 1
    
    return b

def convert_base(n, original_base, new_base, max_power) -> int:
    i = max_power
    result = 0
    while i >= 0:
        denom = new_base ** i
        value = 0
        if denom <= n:
            value = int(n / denom)
            n = n - value * denom
        result += value * original_base ** i
        i -= 1
    return result

l = [1, 13, 4 ** 4 - 1, 16]
print(sort_nToP(l, len(l), 4))
